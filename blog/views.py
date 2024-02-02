from django.shortcuts import render, get_object_or_404
from django.views import generic
from .forms import CommentForm
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

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )
