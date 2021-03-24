"""
This module manages the URLS of the blog application.

:var urlpatterns list: List of all pages linked with the BlogListView view.
"""

from django.urls import path
from .views import BlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'), # Linking the home page with the BlogListView view.
]
