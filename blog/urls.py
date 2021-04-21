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
    HomePageView,
)

urlpatterns = [
    # Linking a blog post with the BlogDetailView view and the template post_detail.
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    # Linking the blog page with the BlogListView view and the template blog_list.
    path('blog/', BlogListView.as_view(), name='blog_list'),
    # Linking the home page with the HomePageView view and the template home.
    path('', HomePageView.as_view(), name='home'),
]
