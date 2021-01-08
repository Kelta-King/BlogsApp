from django.shortcuts import render
from .models import Article

# Create your views here.

def articles_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

def hey(request):
    return render(request, 'articles/hey.html')