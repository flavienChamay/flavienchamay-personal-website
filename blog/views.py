"""
This module manages the views of the blog application.

:class BlogListView: The class view that will be used for the class Post.
"""

from django.views.generic import ListView, DetailView
from .models import Post

class BlogListView(ListView):
    """
    Class view that links the Post class to the home.html file.

    :var model Post: The model of the ListView.
    :var template_name str: The template used for this view.
    """
    
    model = Post
    template_name = 'home.html'

    
class BlogDetailView(DetailView):
    """
    Class view that links the Post class to the post_detail.html template file.

    :var mode Post: The model of the DetailView.
    :var template_name str: The template used for this view.
    """
    
    model = Post
    template_name = 'post_detail.html'
