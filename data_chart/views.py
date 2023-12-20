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
    
from django.http import JsonResponse
from django.db.models.functions import TruncHour
from django.db.models import Count
from .models import Order

def order_per_hour_chart_data(request):
    data = Order.objects.annotate(hour=TruncHour('created_at')).values('hour').annotate(count=Count('id')).order_by('hour')
    
    labels = [d['hour'].strftime('%Y-%m-%d %H:%M:%S') for d in data]
    values = [d['count'] for d in data]
    
    return JsonResponse(data={'labels': labels, 'values': values})

from django.views.generic import TemplateView
from django.db.models.functions import ExtractHour
from django.db.models import Count
from orders.models import Order
from django.utils import timezone

class HourlyOrdersChartView(TemplateView):
    template_name = 'data_chart/hourly_orders_chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Assuming you want to display data for the current day
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
        
        # Prepare data for the chart
        hours = list(range(24))  # 0..23 for all hours in a day
        counts = [0]*24  # initialize all counts to 0
        for item in hourly_data:
            counts[item['hour']] = item['count']
        
        # Store hours and counts in context to pass to the template
        context['hours'] = hours
        context['counts'] = counts
        
        return context