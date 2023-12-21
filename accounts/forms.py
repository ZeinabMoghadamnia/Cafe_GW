from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomerUser
from django import forms


# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomerUser
#         fields = ('first_name','last_name','username', 'birth_day', 'email','phone_number','city','address','image')


class UserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)
    password2 = forms.CharField(label='تکرار رمز عبور', widget=forms.PasswordInput)
    class Meta:
        model = CustomerUser
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'birth_day', 'city', 'address', 'image']
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'email': 'ایمیل',
            'phone_number': 'شماره تلفن',
            'birth_day': 'تاریخ تولد',
            'city': 'شهر',
            'address': 'آدرس',
            'image': 'تصویر',
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomerUser
        fields = ('birth_day', 'email','phone_number','city','address','image','user_type')
        labels = {
            'email': 'ایمیل',
            'birth_day': 'تاریخ تولد',
            'city': 'شهر',
            'address': 'آدرس',
            'image': 'تصویر',
            'user_type': 'نوع کاربری',
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label="ایمیل یا شماره تلفن")
    password = forms.CharField(max_length=50, label="رمز عبور", widget=forms.PasswordInput)

