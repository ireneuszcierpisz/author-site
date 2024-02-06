from django.shortcuts import render
from .models import Excerpt


def excerpt_from(request):
    """
    Renders the Excerpt page
    """
    excerpt = Excerpt.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "excerpt/excerpt.html",
        {"excerpt": excerpt},
    )
