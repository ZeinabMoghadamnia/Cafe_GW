from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import DetailView, TemplateView


# Create your views here.

class HomePage(TemplateView):
    template_name = 'cafemenu/main_page.html'
    
class Contact(TemplateView):
    template_name = 'cafemenu/contact.html'

# def home_page(request):
#     return render(request, 'cafemenu/main_page.html')

# def contact(request):
#     return render(request, 'cafemenu/contact.html')