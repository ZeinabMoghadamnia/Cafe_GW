from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, FormView
from cafemenu.models import Category
from .forms import ForrmatForm, FormGetDate
from .admin import PostResourse
from django.urls import reverse_lazy
from django.core.paginator import Paginator


class HomePage(ListView, FormView):
    template_name = "home/home.html"
    form_class = ForrmatForm
    success_url = reverse_lazy("home:home")


    def get_queryset(self, start_date=None, end_date=None):
        if start_date and end_date:
            return Category.objects.filter(created__gte=start_date, created__lte=end_date)

        else:
            return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form2'] = FormGetDate()
        return context

    def post(self, request, **kwargs):

        if 'download' in request.POST:
            forms = FormGetDate(request.POST)
            if forms.is_valid():
                qs = self.get_queryset(start_date=forms.cleaned_data['date1'], end_date=forms.cleaned_data['date2'])

            else:
                qs = self.get_queryset()
        elif 'show' in request.POST:
            forms = FormGetDate(request.POST)
            form = ForrmatForm()
            if forms.is_valid():
                qs = self.get_queryset(start_date=forms.cleaned_data['date1'], end_date=forms.cleaned_data['date2'])
                # HomePage.start_date = forms.cleaned_data['date1']
                # HomePage.end_date = forms.cleaned_data['date2']
                return render(request, self.template_name, {"date": qs, "form2": forms, 'form': form})
            else:
                qs = self.get_queryset()

        else:
            qs = self.get_queryset()
        # paginator = Paginator(qs, 2)
        # page_number = request.GET.get("page")
        # page_obj = paginator.get_page(page_number)
        dataset = PostResourse().export(qs)
        format = request.POST.get("format")
        if format == 'xls':
            ds = dataset.xls
        elif format == "csv":
            ds = dataset.csv
        elif format == 'json':
            ds = dataset.json
        else:
            ds = dataset.xls
            format = 'xls'
        response = HttpResponse(ds, content_type=f'{format}')
        response['Content-Disposition'] = f"attachment; filename=posts.{format}"
        return response
