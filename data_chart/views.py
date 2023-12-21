from django.shortcuts import render
from django.views.generic import ListView
from accounts.models import CustomerUser
from datetime import date



class ChartListView(ListView):
    model = CustomerUser
    template_name = 'data_chart/../report/templates/home/chart_list.html'
    context_object_name = 'user_data'


    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        age_groups = {'0-10': 0, '11-20': 0, '21-30': 0, '31-40': 0, '41+': 0}
        today = date.today()
        
        for user in context['user_data']:
            age = today.year - user.birth_day.year - ((today.month, today.day) < (user.birth_day.month, user.birth_day.day))
            if age <= 10:
                age_groups['0-10'] += 1
            elif age <= 20:
                age_groups['11-20'] += 1
            elif age <= 30:
                age_groups['21-30'] += 1
            elif age <= 40:
                age_groups['31-40'] += 1
            else:
                age_groups['41+'] += 1

        context['labels'] = list(age_groups.keys())
        context_data = list(age_groups.values())
        context['data'] = context_data
        return context

from django.views.generic import TemplateView
from django.db.models.functions import ExtractHour
from django.db.models import Count
from orders.models import Order
from django.utils import timezone

class HourlyOrdersChartView(TemplateView):
    template_name = 'hourly_orders_chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        today_min = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        today_max = timezone.now().replace(hour=23, minute=59, second=59, microsecond=999999)

        hourly_data = (
            Order.objects
            .filter(created_at__range=(today_min, today_max))
            .annotate(hour=ExtractHour('created_at'))
            .values('hour')
            .annotate(count=Count('id'))
            .order_by('hour')
        )
        
        hours = list(range(24))
        counts = [0]*24 
        for item in hourly_data:
            counts[item['hour']] = item['count']
        
        context['hours'] = hours
        context['counts'] = counts
        
        return context