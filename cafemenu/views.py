from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def home_page(request):
    return render(request, 'cafemenu/main_page.html')