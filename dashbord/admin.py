from django.contrib import admin
from Cafe_GW.cafemenu.models import MenuItem
from import_export import resources
# Register your models here.
class PostResourse(resources.ModelResource):
    class Meta:
        model =MenuItem
        fields = ("id","title", "description" ,"is_active" , "created")
        export_order = ("id","description" ,"is_active" ,"title", "created")

admin.site.register(MenuItem)