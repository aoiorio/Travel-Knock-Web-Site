from django.shortcuts import render
from django.views.generic import TemplateView

# Home Page
class HomeView(TemplateView):
    template_name = 'home/home.html'

class KnockDetailsView(TemplateView):
    template_name = 'knock_details/knock_details.html'

class CreatePlansDetailsView(TemplateView):
    template_name = 'create_plans_details/create_plans_details.html'