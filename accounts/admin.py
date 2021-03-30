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
    :var list_display list: List of the fields that we can control and see in the administration.
    :var fieldsets dict: Used to to edit and add new custom fields.
    :var add_fieldsets dict: Used to to edit and add new custom fields.
    """
    
    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'is_staff', ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age', )}),
    )
    

# Register the new functionalities into the site.
admin.site.register(CustomUser, CustomUserAdmin)
