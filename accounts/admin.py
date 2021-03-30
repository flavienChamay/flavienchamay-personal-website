"""
This module extends the existing UserAdmin class to use our new CustomUser model.

:class: CustomUserAdmin(UserAdmin)
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """
    Class that adds new the functionalities of CustomUser to the admin users.

    :var add_form CustomUserCreationForm: What form to use when creating an admin.
    :var form CustomUserChangeForm: What form to use when changing the admin.
    :var model CustomUser: The model of the admin.
    """
    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

# Register the new functionalities into the site.
admin.site.register(CustomUser, CustomUserAdmin)
