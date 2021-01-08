from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles_list),
    path('hello', views.hey),
]
