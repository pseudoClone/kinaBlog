from django.contrib import admin

# models.py defines your database models. admin.py registers your models with the Django admin
# Basically register the model in to the admin area
from .models import Post

admin.site.register(Post) # Make blog post accessible to the admin area
