"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

This module links all the apps to the website.

:var urlpatterns list: List of all URLS links for the website.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Link to the URL of the site administration.
    path('admin/', admin.site.urls),
    # Link to the URL for login.
    path('accounts/', include('django.contrib.auth.urls')),
    # Link to the URLS of the blog app.
    path('', include('blog.urls')), 
]
