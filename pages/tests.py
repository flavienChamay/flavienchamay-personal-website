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
        This function sets the variables that will be reused for the next tests.

        :var url URL: URL of the home page.
        :var response request.Reponse: The response after accessing the URL of the home page.
        :returns: None.
        """

        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        """
        This function tests if the response returns a 200 status code.

        :returns: None.
        """

        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        """
        This function tests if the home page uses the home.html template.

        :returns: None.
        """

        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        """
        This function tests if the home page contains a correct phrase.

        :returns: None.
        """

        self.assertContains(
            self.response, 'Flavien Chamay\'s Personal Website')

    def test_homepage_does_not_contains_incorrect_html(self):
        """
        This function tests if the home page does not contains a certain phrase.

        :retuns: None.
        """

        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.'
        )

    def test_homepage_url_resolves_homepagesview(self):
        """
        This function tests if the home page uses the correct view.

        :var view: The view at the / URL.
        :returns: None.
        """

        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


class AboutpageTests(SimpleTestCase):
    """
    This class inherits from the SimpleTestCase.

    :method: setUp(self)
    :method: test_aboutpage_status_code(self)
    :method: test_aboutpage_template(self)
    :method: test_aboutpage_contains_correct_html(self)
    :method: test_aboutpage_does_not_contains_incorrect_html(self)
    :method: test_aboutpage_url_resolves_aboutpagesview(self)
    """

    def setUp(self):
        """
        This function sets the variable used for further tests.

        :returns: None.
        """

        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        """
        This function verifies if the about page has a response of 200.

        :returns: None.
        """

        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        """
        This function verifies if the about page uses the about.html template.

        :returns: None.
        """

        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_html(self):
        """
        This function verifies if the about page contains a correct phrase.

        :returns: None.
        """

        self.assertContains(
            self.response, 'About Page')

    def test_aboutpage_does_not_contains_incorrect_html(self):
        """
        This functions verifies if the about page does not contains a certain phrase.

        :returns: None.
        """

        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.'
        )

    def test_aboutpage_url_resolves_aboutpagesview(self):
        """
        This function verfies if the about page uses the correct view.

        :var view: The view given by the /about/ URL.
        :returns: None.
        """

        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )
