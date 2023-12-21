from django.urls import path, include
from . import views

app_name = "home"
urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
    path('age-chart/', views.ChartListView.as_view(), name='age_report'),
    path('hour-chart/', views.HourlyOrdersChartView.as_view(), name='hour_report'),
]
