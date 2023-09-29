from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = {'name',} #Order items by name in the admin site
    
    def __str__(self):
        return self.name
