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

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from environs import Env

# Environment Variables
env = Env()
env.read_env()

urlpatterns = [
    # Link to the URL of the site administration.
    path(env.str("DJANGO_ADMIN_URL_HARDENING"), admin.site.urls),
    # Link to the URL for login.
    path('accounts/', include('django.contrib.auth.urls')),
    # Link to the URLS of the pages app (to the home page more precisely).
    path('', include('pages.urls')),
    # Link to the URLS of the blog app.
    path('blog/', include('blog.urls')),
]

# Trigger django debug toolbar if DEBUG is true
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
