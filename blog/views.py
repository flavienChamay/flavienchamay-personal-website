"""
This module manages the views of the blog application.

:class BlogListView: The class view that will be used for the class Post in the home page.
:class BlogDetailView: The class view that will be used for the class Post in the post_detail.html file.
:class BlogCreateView: The class view that will be used for the class Post in the post_new.html file.
:class BlogUpdateView: The class view that will be used for the class Post in the post_edit.html file.
:class BlogDeleteView: The class view that will be used for the class Post in the post_delete.html file.
:class HomePageView: The class view that will be used for the home page.
"""

from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy
from .models import Post
from django.db.models import Q


class BlogListView(ListView):
    """
    Class view that links the Post class to the home.html file.

    :var model Post: The model of the ListView.
    :var template_name str: The template used for this view.
    :var ordering list: Order the posts from newest to oldest.
    :var paginate_by int: The number of posts for each page.
    """

    model = Post
    template_name = 'blog_list.html'
    ordering = ['-date_publication']
    paginate_by = 10


class BlogDetailView(DetailView):
    """
    Class view that links the Post class to the post_detail.html template file.

    :var model Post: The model of the DetailView.
    :var template_name str: The template used for this view.sh
    """

    model = Post
    template_name = 'blog_detail.html'


class SearchResultsListView(ListView):
    """
    Class view that links the search bar of the blog to the search results.

    :var model Post: The model of the ListView.
    :var context_object_name str: The name of the object.
    :var template_name str: The template used for this view.
    """

    model = Post
    context_object_name = 'blog_list'
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(
            Q(title__icontains=query)
        )


class SearchBarView(TemplateView):
    """
    Class view that links the Blog app to the search bar.

    :var template_name str: The template used for this view.
    """

    template_name = 'search_bar.html'
