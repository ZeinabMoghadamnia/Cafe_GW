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
    