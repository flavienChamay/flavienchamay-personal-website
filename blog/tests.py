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
    :method: test_get_absolute_url(self)
    :method: test_post_create_view(self)
    :method: test_post_update_view(self)
    :method: test_post_delete_view(self)
    """

    def setUp(self):
        """
        This function sets fills the variables of the database for further testing.

        :var user User: The user of the post filled with infos.
        :var post Post: The post to be tested and filled with infos.
        :returns: None.
        """

        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title='A good title',
            body='Nice body content',
        )

    def test_string_representation(self):
        """
        This function compares the title of a post and its representation.

        :var post Post: A post is created with a title.
        :return: None.
        """

        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        """
        This function verifies if the title and the body of a post are properly saved.

        :returns: None.
        :notes: Can find a way to test the date_publication variable. Is it necessary or not?
        """

        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.body}', 'Nice body content')

    def test_post_list_view(self):
        """
        This function tests if the client gets the correct response if he visits the home page, if he get the correct body of the post and if the template is the correct one.

        :var response: The response a client get when he tries to access the home page.
        :returns: None.
        """

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        """
        This function tests if the client gets the proper response when he visits a post, if he gets no response then he must reveive the proper error handling.

        :var response request.Reponse: The response for the client after accessing the post 1.
        :var no_response request.Response: The response after accessing the wrong post.
        :returns: None.
        """

        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_get_absolute_url(self):
        """
        This function targets the first post of the database to launch further tests.

        :returns: None
        """
        
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    def test_post_create_view(self):
        """
        This function tests the creation of a new view for a post, it ensures that the title and body is properly created.

        :response request.Response: The response filled with a body and a title.
        :returns: None.
        """
        
        response = self.client.post(reverse('post_new'), {
            'title': 'New title',
            'body': 'New text',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'New title')
        self.assertEqual(Post.objects.last().body, 'New text')

    def test_post_update_view(self):
        """
        This function tests the updating of a view for the first post and updates its body and  title and tests if it returns a proper status code (302 for a redirection).

        :var response request.Response: The response updated with a new body and title.
        :returns: None.
        """
        
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': 'Updated title',
            'body': 'Updated text',
        })
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        """
        This function tests the deletion of a view for the first post and if it returns a proper status code (302 is a redirection since the item no longer exists).

        :var response request.Response: The response that delete the first post.
        :returns: None.
        """
        
        response = self.client.post(
            reverse('post_delete', args='1')
        )
        self.assertEqual(response.status_code, 302)
