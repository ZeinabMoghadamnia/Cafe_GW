from django.shortcuts import render

from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, FormView
from Cafe_GW.cafemenu.models import MenuItem
from .forms import ForrmatForm
from .admin import PostResourse


class HomePage(ListView, FormView):
    model = Post
    template_name = "home/home.html"
    form_class = ForrmatForm

    def post(self, request, **kwargs):
        qs = self.get_queryset()
        dataset = PostResourse().export(qs)

        format = request.POST.get("format")

        if format == 'xls':
            ds = dataset.xls
        elif format == "csv":
            ds = dataset.csv
        else:
            ds = dataset.json

        response = HttpResponse(ds, content_type=f'{format}')
        response['Content-Disposition'] = f"attachment; filename=posts.{format}"
        return response

