from django.urls import path
from .views import HomePage, Contact

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('contact/', Contact.as_view(), name='contact'),
]
