from django.db import models
# Now lets connect to the user that we just created(i.e admin)
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length = 255)
    author = models.ForeignKey(User, on_delete = models.CASCADE) # On deletion of the user the post are deleted too with the CASCADE option
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + self.author # This shows up in the admin page
