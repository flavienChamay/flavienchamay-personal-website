"""
This module manages the views of the pages application.

:class HomePageView: The class view that will be used for the home page.
:class AboutPageView: The class view that will be used for the about page.
"""


from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """
    Class view linked to home.html file.

    :var template_name str: The template used for this view.
    """

    template_name = 'home.html'


class AboutPageView(TemplateView):
    """
    Class view linked to about.html file.

    :var template_name str: The template used for this view.
    """

    template_name = 'about.html'
