from django.urls import path
from .views import HomePage, Contact, CategoryView, CategoryDetailView, ItemsView, ItemsDetailView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('contact/', Contact.as_view(), name='contact'),
    path('category/', CategoryView.as_view(), name='category'),
    path('category/<slug:category_slug>/', CategoryDetailView.as_view(), name='category-detail'),
    path('all-items/', ItemsView.as_view(), name='all-items'),
    path('items/<slug:slug>/', ItemsDetailView.as_view(), name='item-detail'),
]
