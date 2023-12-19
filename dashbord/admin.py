from django.contrib import admin
from cafemenu.models import Category
from import_export import resources


# Register your models here.
class PostResourse(resources.ModelResource):
    class Meta:
        model = Category
        fields = ("title", "description", "is_active", "created")
        export_order = ("description", "is_active", "title", "created")

