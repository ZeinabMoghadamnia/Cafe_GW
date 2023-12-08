from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)  # ask abolfazl
    updated_at = models.DateTimeField(auto_now=True)    # ask abolfazl
    # slug = models.SlugField()    # ask abolfazl
    
    def __str__(self):
        return self.category_name()


class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menuitem') # ask abolfazl for related name and first item
    item_name = models.CharField(max_length=150)
    price = models.IntegerField()
    mojoudi = models.IntegerField()
    # slug = models.SlugField()    # ask abolfazl
    
    def __str__(self):
        return f'{self.item_name()}'


class Image(models.Model):
    path = models.CharField(max_length=255)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='image')    # ask abolfazl
    
    
# class ShoppingCart(models.Model):
#     item_id = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='shoppingcart')    # ask abolfazl
#     quantity = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True) # ask abolfazl
#     updated_at = models.DateTimeField(auto_now=True)    # ask abolfazl
#     total_price = models.IntegerField()