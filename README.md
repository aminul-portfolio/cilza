# Cilza Cakes Studio (healthcakes_project)

Premium bakery e-commerce demo website built with Django.

## Website Purpose

This project presents a modern cake storefront for Cilza Cakes Studio.  
It demonstrates:
- premium product browsing and category filtering
- consistent responsive layout across pages
- contact and order-planning user flows
- basic accessibility and privacy-policy coverage for coursework submission

## Tech Stack

- Python
- Django
- Bootstrap
- WhiteNoise (static file serving in production)
- PostgreSQL (Render production database)
- SQLite (local fallback)

## Run Locally

1. Create and activate a virtual environment.
2. Install dependencies:
   - `pip install -r healthcakes_project/requirements.txt`
3. Move into the Django project folder:
   - `cd healthcakes_project`
4. Run migrations:
   - `python manage.py migrate`
5. Start development server:
   - `python manage.py runserver`
6. Open:
   - [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Virtual Environment

If you use the expected local environment path:

- `G:\healthcakes_project\.venv312\Scripts\Activate.ps1`

## Dependencies

See `requirements.txt` for production-ready pinned dependencies.

## Folder Structure

- `healthcakes_project/` - Django project root (settings, urls, manage.py)
- `healthcakes_project/cakes/` - main app (templates, static, views, models)
- `submission_evidence/` - testing and submission evidence notes
- `.venv312/` - local virtual environment (development only)

## Main Pages and Features

- Home (`/`)
- Cakes listing with filters (`/cakes/`)
- Cake detail pages (`/cakes/<slug>/`)
- Occasions (`/welcome/`)
- Offers (`/offers/`)
- About (`/about/`)
- Contact (`/contact/`)
- Cart (`/cart/`) - localStorage-backed demo cart view
- Plan an Order (`/plan-order/`) - demo request form
- Privacy Policy (`/privacy/`)

## Accessibility and UX Notes

- Semantic `header/nav/main/footer` structure in shared base template.
- One primary `h1` per page template.
- Keyboard-visible focus states for links, buttons, and form controls.
- Form labels are present (no placeholder-only core fields).

## Known Limitations

- Some hero/gallery image assets referenced by templates may need to be added under static images for full visual parity.
- Contact and plan-order forms are front-end validated demo flows and do not persist submissions.
- Cart uses browser `localStorage` (demo) rather than server-side order persistence.
- `SECRET_KEY` is currently a development value in settings and should be moved to environment variables for production.

## Live Deployment

Not deployed yet.

## Render Deployment

Repository:
- [https://github.com/aminul-portfolio/cilza.git](https://github.com/aminul-portfolio/cilza.git)

Render blueprint file:
- `render.yaml` (repository root)

Render Django root:
- `healthcakes_project`

### Render Build Command

- `bash build.sh`

### Render Start Command

- `python -m gunicorn healthcakes_project.asgi:application -k uvicorn.workers.UvicornWorker`

### Required Environment Variables

- `SECRET_KEY`
- `DATABASE_URL`
- `WEB_CONCURRENCY`
- `DJANGO_ALLOWED_HOSTS`

### Demo Data

This project includes an idempotent seed command:

- `python manage.py seed_demo_data`

The current `build.sh` runs this after migrations so first deploy can populate demo cakes.

### Local setup sequence

From repository root:

1. `cd healthcakes_project`
2. `python manage.py migrate`
3. `python manage.py seed_demo_data`
4. `python manage.py runserver`

## Media / Asset Credits

- Demo bakery visuals are placeholders for educational use.
- Replace with licensed or original media before production release.
