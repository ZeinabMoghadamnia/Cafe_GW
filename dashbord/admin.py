from django.contrib import admin
from cafemenu.models import Category
from import_export import resources


# Register your models here.
class PostResourse(resources.ModelResource):
    class Meta:
        model = Category
        fields = ("category_name", "created_at")
        export_order = ("created_at", "category_name")
