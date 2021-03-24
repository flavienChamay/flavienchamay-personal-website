from django.db import models
from django.urls import reverse

class Post(models.Model):
    """
    Post class is used to create a post in the blog application.

    :method: __str__(self)
    :method: get_absolute_url(self)
    :var title CharField: The title of the post, with a maximum length of 200 characters.
    :var date_publication DateTimeField: Date and time of publication of the post.
    :var body TextField: The body of the post containing text.
    """
    
    title = models.CharField(max_length=200)
    date_publication = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

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
        
        return reverse('post_detail', args=[str(self.id)])
