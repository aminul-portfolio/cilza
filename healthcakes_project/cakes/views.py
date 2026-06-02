from django.core.paginator import Paginator
from django.db.models import Avg, Q
from django.shortcuts import render, get_object_or_404, redirect

from .models import Cake, CakeVariant, CakeCollection, Review
from .forms import ReviewForm


def home(request):
    return render(request, "cakes/home.html")


def cake_list(request):
    """
    All cakes page with server-side category filter, keyword search,
    and pagination.
    """
    search_query = request.GET.get("q", "").strip()
    active_category = request.GET.get("category", "").strip().lower()

    cakes_qs = (
        Cake.objects
        .filter(is_active=True)
        .prefetch_related("variants", "collections")
        .order_by("name")
    )

    if active_category and active_category != "all":
        cakes_qs = cakes_qs.filter(
            Q(occasion_type__iexact=active_category) |
            Q(collections__key__iexact=active_category)
        ).distinct()

    if search_query:
        cakes_qs = cakes_qs.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(short_description__icontains=search_query) |
            Q(category__icontains=search_query) |
            Q(collections__label__icontains=search_query)
        ).distinct()

    total_results = cakes_qs.count()
    paginator = Paginator(cakes_qs, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    collections = (
        CakeCollection.objects
        .filter(is_active=True)
        .order_by("sort_order")
    )

    return render(
        request,
        "cakes/cakes.html",
        {
            "cakes": page_obj.object_list,
            "page_obj": page_obj,
            "collections": collections,
            "search_query": search_query,
            "active_category": active_category,
            "total_results": total_results,
        },
    )


def cake_detail(request, slug):
    """
    Single cake detail:
    - Uses the hero layout + tabs.
    - Shows only approved reviews.
    - Handles review form POST and redirects back to the same page.
    - Shows up to 4 related cakes with same occasion_type.
    """
    cake = get_object_or_404(Cake, slug=slug, is_active=True)

    # Variants for the dropdown + default for price display
    variants = cake.variants.all().order_by("price")
    default_variant = cake.default_variant()

    # Approved reviews only
    reviews = cake.reviews.filter(is_approved=True)
    review_count = reviews.count()
    average_rating = (
        reviews.aggregate(avg=Avg("rating"))["avg"] if review_count else None
    )

    # Handle review form
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.cake = cake
            # is_approved default (False/True) is handled by the model
            review.save()
            return redirect("cake_detail", slug=cake.slug)
    else:
        review_form = ReviewForm()

    # Related cakes – same occasion type, different cake
    related_cakes = (
        Cake.objects.filter(is_active=True, occasion_type=cake.occasion_type)
        .exclude(id=cake.id)
        .order_by("name")[:4]
    )

    return render(
        request,
        "cakes/cake_detail.html",
        {
            "cake": cake,
            "variants": variants,
            "default_variant": default_variant,
            "reviews": reviews,
            "review_count": review_count,
            "average_rating": average_rating,
            "review_form": review_form,
            "related_cakes": related_cakes,
        },
    )


def offers(request):
    return render(request, "cakes/offers.html")


def about(request):
    return render(request, "cakes/about.html")


def contact(request):
    return render(request, "cakes/contact.html")


def welcome(request):
    return render(request, "cakes/welcome.html")


def privacy(request):
    return render(request, "cakes/privacy.html")


def cart(request):
    return render(request, "cakes/cart.html")


def plan_order(request):
    return render(request, "cakes/plan_order.html")
