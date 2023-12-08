from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomerUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomerUser
    list_display = ['username', 'email', 'birth_day', 'phone_number']
    fieldsets = UserAdmin.fieldsets + (
        ('Others', {'fields': ('birth_day','phone_number','city','address','image', 'user_type')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('birth_day','phone_number','city','address','image')}),
    )


admin.site.register(CustomerUser, CustomUserAdmin)