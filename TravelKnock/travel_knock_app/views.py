from django.shortcuts import render
from django.views.generic import TemplateView

# Home Page
class HomeView(TemplateView):
    template_name = 'home/home.html'