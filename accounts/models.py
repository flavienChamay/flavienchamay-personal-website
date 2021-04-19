from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Class that manages the custom user model for the entire site. Even if this site will not use a custom user model we must implement it for further improvements (if needed).
    """
    
    pass
