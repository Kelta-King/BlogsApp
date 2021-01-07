from django.urls import path
from . import views

urlpatterns = [
    path('Articles/', views.article_list),
]
