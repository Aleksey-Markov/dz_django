
from django.urls import path
from blog.apps import BlogConfig
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('blog/posts/', PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('create/', PostCreateView.as_view(), name='create_post'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='update_post'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete_post')
]
