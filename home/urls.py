from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('countries/', views.scrape_countries, name='countries'),
    path('stjoes', views.stjoes, name='stjoes'),
]
