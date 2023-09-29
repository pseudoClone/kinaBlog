from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = {'name',} #Order items by name in the admin site
    
    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True) #If user enters nothing in the description, then its fine too
    price = models.FloatField()
    isSold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User,related_name = 'items', on_delete = models.CASCADE)
    # Foreign key of user.
    # Getting the items for a users will be easy with the related_name field
    # If user if deleted, all of their items are also deleted
    # Will soon import User
    created_date = models.DateTimeField(auto_now_add=True)
