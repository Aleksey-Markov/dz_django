from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Post


class PostListView(ListView):
    model = Post

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'content', 'preview', 'created_at', 'is_published')
    success_url = reverse_lazy('blog:posts')

    def form_valid(self, form):
        if form.is_valid():
            post = form.save()
            post.slug = slugify(post.title)
            post.save()

        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'content', 'preview', 'created_at', 'is_published')

    def get_success_url(self):
        return reverse('blog:post', args=[self.kwargs.get('pk')])

    def form_valid(self, form):
        if form.is_valid():
            post = form.save()
            post.slug = slugify(post.title)
            post.save()

        return super().form_valid(form)


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:posts')
