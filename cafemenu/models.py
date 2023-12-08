from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.category_name()


class MenuItem(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Category')
    item_name = models.CharField(max_length=150)
    price = models.IntegerField()
    mojoudi = models.IntegerField()
    
    def __str__(self):
        return f'{self.item_name()}'

