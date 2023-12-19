from django.urls import path
from .views import ChartListView

urlpatterns = [
    path('', ChartListView.as_view(), name='report'),
]