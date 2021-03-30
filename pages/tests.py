"""
Module that tests the pages app.

:class: HomePageTests(SimpleTestCase)
"""

from django.test import TestCase
from django.urls import reverse

class HomePageTests(TestCase):
    """
    Class that tests the home page in regard to the pages app.

    :method: test_home_page_status_code(self)
    :method: test_view_url_by_name(self)
    :method: test_view_uses_correct_template(self)
    """
    
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
