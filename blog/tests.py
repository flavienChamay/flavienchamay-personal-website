"""
This module manages the tests for the blog app.

:class BlogTests: The class that will be used for testing the blog app.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post


class BlogTests(TestCase):
    """
    This class inherits from TestCase for testing database of the Post model.

    :method: setUp(self)
    :method: test_string_representation(self)
    :method: test_post_content(self)
    :method: test_post_list_view(self)
    :method: test_post_detail_view(self)
    """
    
    def setUp(self):
        """
        This function sets fills the variables of the database for further testing.

        :var user User: The user of the post filled with infos.
        :var post Post: The post to be tested and filled with infos.
        """
        
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@email.com',
            password = 'secret'
        )

        self.post = Post.objects.create(
            title = 'A good title',
            body = 'Nice body content',
        )

    def test_string_representation(self):
        """
        This function compares the title of a post and its representation.

        :var post Post: A post is created with a title.
        """
        
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        """
        This function verifies if the title and the body of a post are properly saved.

        :notes: Can find a way to test the date_publication variable. Is it necessary or not?
        """
        
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.body}', 'Nice body content')

    def test_post_list_view(self):
        """
        This function 

        :var response:
        """
        
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        """
        This function

        :var response:
        :var no_response:
        """
        
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')
            
