from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'blog/index.html'
class PostDetail(DetailView):
    model = Post

# Create your views here.
