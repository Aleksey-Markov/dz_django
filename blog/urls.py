
from django.urls import path
from blog.apps import BlogConfig
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView

app_name = BlogConfig.name

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='update'),
]
