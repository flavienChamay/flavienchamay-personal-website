"""
This module manages the tests of the pages app.

:class HomepageTests: Class that will be used for testing the home page.
:class AboutpageTests: Class that will be used for testing the about page.
"""

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView


class HomepageTests(SimpleTestCase):
    """
    This class inherits from SimpleTestCase for testing the home page.

    :method: setUp(self):
    :method: test_homepage_status_code(self)
    :method: test_homepage_template(self)
    :method: test_homepage_contains_correct_html(self)
    :method: test_homepage_does_not_contains_incorrect_html(self)
    :method: test_homepage_url_resolves_homepagesview(self)
    """

    def setUp(self):
        """
        This function sets fills the variables of the 
        """

        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(
            self.response, 'Flavien Chamay\'s Personal Website')

    def test_homepage_does_not_contains_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.'
        )

    def test_homepage_url_resolves_homepagesview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


class AboutpageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(
            self.response, 'About Page')

    def test_aboutpage_does_not_contains_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.'
        )

    def test_aboutpage_url_resolves_aboutpagesview(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )
