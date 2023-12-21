from django.urls import path
from .views import ChartListView, HourlyOrdersChartView

urlpatterns = [
    path('', HourlyOrdersChartView.as_view(), name='report'),
]