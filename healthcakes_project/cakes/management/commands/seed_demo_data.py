import shutil
from pathlib import Path

from django.core.management.base import BaseCommand
from django.conf import settings

from cakes.content import cakes_data, load_initial_cakes


class Command(BaseCommand):
    help = "Seed demo cake collections, cakes, and variants."

    def handle(self, *args, **options):
        # Ensure referenced demo images exist under MEDIA_ROOT/cakes
        media_cakes_dir = Path(settings.MEDIA_ROOT) / "cakes"
        media_cakes_dir.mkdir(parents=True, exist_ok=True)

        static_img_dir = Path(settings.BASE_DIR) / "cakes" / "static" / "img"
        for cake in cakes_data:
            image_path = cake.get("image", "")
            image_name = Path(image_path).name
            if not image_name:
                continue
            src = static_img_dir / image_name
            dst = media_cakes_dir / image_name
            if src.exists():
                shutil.copy2(src, dst)

        load_initial_cakes()

        from cakes.models import Cake

        for cake_data in cakes_data:
            image_rel = cake_data.get("image", "")
            if not image_rel:
                continue
            media_file = media_cakes_dir / Path(image_rel).name
            if not media_file.exists():
                continue
            try:
                cake = Cake.objects.get(slug=cake_data["slug"])
            except Cake.DoesNotExist:
                continue
            needs_image = not cake.main_image
            if cake.main_image:
                try:
                    needs_image = not Path(cake.main_image.path).exists()
                except (ValueError, FileNotFoundError):
                    needs_image = True
            if needs_image:
                cake.main_image = image_rel
                cake.save(update_fields=["main_image"])
        self.stdout.write(self.style.SUCCESS("Demo cake data seed completed."))
