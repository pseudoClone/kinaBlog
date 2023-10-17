from django.db import models
# Now lets connect to the user that we just created(i.e admin)
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length = 255)
    title_tag = models.CharField(max_length = 255, default = 'pseudoBlog')
    author = models.ForeignKey(User, on_delete = models.CASCADE) # On deletion of the user the post are deleted too with the CASCADE option
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author) # This shows up in the admin page

    def get_absolute_url(self):
        return reverse('article-detail', args = (str(self.id))) # Pointing to the location to go after posting
    # Every post has an id so this function asks for one more argument i.e the id
