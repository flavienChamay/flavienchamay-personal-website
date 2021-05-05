import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import timezone
from taggit.managers import TaggableManager


class Post(models.Model):
    """
    Post class is used to create a post in the blog application.

    :method: __str__(self)
    :method: get_absolute_url(self)
    :var title CharField: The title of the post, with a maximum length of 200 characters.
    :var date_publication DateTimeField: Date and time of publication of the post.
    :var body TextField: The body of the post containing text.
    :var author str: The author of the post, by default is Flavien Chamay.
    :var date_publication DateTimeField: The date of publication or of modification of the post.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)
    author = models.CharField(default='Flavien Chamay',
                              max_length=200, editable=True)
    date_publication = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    # Tag mechanism
    slug = models.SlugField(unique=True, max_length=100)
    tags = TaggableManager()

    def __str__(self):
        """ 
        Function that designate a post by its title for better readability.

        :returns CharField: The title of the post.
        """

        return self.title

    def get_absolute_url(self):
        """ 
        Function that sets a canonical URL for the post object for having the same reference to the object.

        :returns URL: The canonical URL designating the post object.
        """

        return reverse('blog_detail', args=[str(self.id)])
