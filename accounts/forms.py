"""
This module manages the forms for the creation and updates of accounts on the website.

:class: CustomUserCreationForm(UserCreationForm)
:class: CustomUserChangeForm(UserChangeForm)
"""

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    Class managins the form for the creation of a new user.

    :class: Meta(UserCreationForm)
    """

    class Meta(UserCreationForm):
        """
        This class overridesthe default fields of the users.

        :var model CustomUser: The model to adopt, , we get the current model of the user.
        :var fields ??: The fields to adopt for the form.
        """

        model = get_user_model()
        fields = UserCreationForm.Meta.fields


class CustomUserChangeForm(UserChangeForm):
    """
    Class managing the form for the update of a user.

    :class: Meta
    """

    class Meta:
        """
        This class overrides the default fields for the users.

        :var model CustomUser: The model to adopt, we get the current model of the user.
        :var fields ??: The fields to adopt for the form.
        """

        model = get_user_model()
        fields = UserChangeForm.Meta.fields
