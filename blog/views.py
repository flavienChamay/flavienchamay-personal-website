"""
This module manages the views of the blog application.

:class BlogListView: The class view that will be used for the class Post in the home page.
:class BlogDetailView: The class view that will be used for the class Post in the post_detail.html file.
:class BlogCreateView: The class view that will be used for the class Post in the post_new.html file.
:class BlogUpdateView: The class view that will be used for the class Post in the post_edit.html file.
:class BlogDeleteView: The class view that will be used for the class Post in the post_delete.html file.
"""

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from .models import Post


class HomePageView(TemplateView):
    """
    """
    
    template_name = 'home.html'


class BlogListView(ListView):
    """
    Class view that links the Post class to the home.html file.

    :var model Post: The model of the ListView.
    :var template_name str: The template used for this view.
    """

    model = Post
    template_name = 'blog_list.html'


class BlogDetailView(DetailView):
    """
    Class view that links the Post class to the post_detail.html template file.

    :var model Post: The model of the DetailView.
    :var template_name str: The template used for this view.
    """

    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    """
    Class view that links the Post class to the post_new.html template file.

    :var model Post: The model of the CreateView.
    :var template_name str: The template used for this view.
    :var fields list: List of the fields used to create a new post.
    """

    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body']


class BlogUpdateView(UpdateView):
    """
    Class view that links the Post class to the post_edit.html template file.

    :var model Post: The model of the UpdateView.
    :var template_name str: The template used for this view.
    :var fields list: List of the fields used to update a post.
    """
    
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    """
    Class view that links the Post class to the post_delete.html template file.

    :var model Post: The model used for the DeleteView.
    :var template_name str: The template used for this view.
    :var fields list: List of the fields ussed to delete a post.
    """
    
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
