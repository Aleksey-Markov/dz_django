from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from blog.models import Post


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('id')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'slug', 'content', 'preview', 'created_at', 'is_published', 'views_count')
    success_url = reverse_lazy('blog:posts')


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'slug', 'content', 'preview', 'created_at', 'is_published', 'views_count')

    def get_success_url(self):
        return reverse('blog:posts')
