"""
This module manages the URLS of the blog application.

:var urlpatterns list: List of all pages linked with the BlogListView view, the BlogDetailView view.
"""

from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
)

urlpatterns = [
    # Linking a blog post with the BlogDetailView view and the template post_detail.
    path('post/<uuid:pk>/', BlogDetailView.as_view(), name='post_detail'),
    # Linking the blog page with the BlogListView view and the template blog_list.
    path('', BlogListView.as_view(), name='blog_list'),
]
