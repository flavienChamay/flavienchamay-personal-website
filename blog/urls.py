"""
This module manages the URLS of the blog application.

:var urlpatterns list: List of all pages linked with the BlogListView view, the BlogDetailView view.
"""

from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    SearchResultsListView,
    SearchBarView,
)

urlpatterns = [
    # Linking a blog post with the BlogDetailView view and the template post_detail.
    path('<uuid:pk>', BlogDetailView.as_view(), name='blog_detail'),
    # Linking the blog page with the BlogListView view and the template blog_list.
    path('', BlogListView.as_view(), name='blog_list'),
    # Linking the search results with the blog app.
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    # Linking the search bar with the blog app.
    path('search_bar/', SearchBarView.as_view(), name='search_bar'),
]
