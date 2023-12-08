from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomerUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomerUser
        fields = ('first_name','last_name','username', 'birth_day', 'email','phone_number','city','address','image')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomerUser
        fields = ('birth_day', 'email','phone_number','city','address','image','user_type')