"""
Module of the tests of the account app.

:class CustomUserTests: Class implementing tests for the custom user model.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):
    """
    This class inherits from TestCase for testing database of the Post model.

    :method: test_create_user
    :method: test_create_superuser
    """

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='will',
            email='will@email.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_superuser)
