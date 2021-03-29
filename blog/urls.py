"""
This module manages the URLS of the blog application.

:var urlpatterns list: List of all pages linked with the BlogListView view, the BlogDetailView view.
"""

from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

urlpatterns = [
    # Linking the deletion of a blog post with the BlogDeleteView view and the template post_delete.
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    # Linking the update of a blog post with the BlogUpdateView view and the template post_edit.
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    # Linking the creation of a blog post with the BlogCreateView view and the template post_new.
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    # Linking a blog post with the BlogDetailView view and the template post_detail.
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    # Linking the home page with the BlogListView view and the template home.
    path('', BlogListView.as_view(), name='home'),
]
