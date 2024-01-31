from django.shortcuts import render
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
    paginate_by = 4
