"""
This module manages the URLS of the blog application.

:var urlpatterns list: List of all pages linked with the BlogListView view, the BlogDetailView view.
"""

from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView

urlpatterns = [
    # Linking the creation of a blog post with the BlogCreateView view.
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    # Linking a blog post with the BlogDetailView view.
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    # Linking the home page with the BlogListView view.
    path('', BlogListView.as_view(), name='home'),
]
