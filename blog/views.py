from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
# # Create your views here.
# from django.http import HttpResponse
# def index(request):
#     return HttpResponse("Hello, world! It's author blog")


class PostList(generic.ListView):
    queryset = Post.objects.all()
    # template_name = "post_list.html"
    template_name = "blog/index.html"
    paginate_by = 2


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )

