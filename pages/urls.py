"""
This module manages the URLS of the pages application.

:var urlpatterns list: List of all pages linked with the HomePageView view and the AboutPageView view.
"""

from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    # Linking the home page with the HomePageView view and the template home.
    path('', HomePageView.as_view(), name='home'),
    # Linking the about page with the AboutPageView view and the template about.
    path('about/', AboutPageView.as_view(), name='about'),
]
