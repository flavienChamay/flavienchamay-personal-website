"""
Module that manage the URLS of the pages app.

:var urlpatterns list: List of all URLS linked to the pages app.
"""

from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home')
]
