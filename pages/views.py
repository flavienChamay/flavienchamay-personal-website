"""
Module of the views of the pages app.

:class: HomePageView
"""

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    """
    Class of the view of the pages app for the home page.

    :var template_name str: The template used for this view ie home.html.
    """
    
    template_name = 'home.html'
