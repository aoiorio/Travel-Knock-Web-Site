from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("knock/", views.KnockDetailsView.as_view(), name="knock_details"),
]