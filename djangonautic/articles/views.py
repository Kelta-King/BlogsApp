from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# Create your views here.

def articles_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

def hey(request):
    return render(request, 'articles/hey.html')

def articles_details(request, page):

    article = Article.objects.get(slug = page)
    return render(request, 'articles/article.html', {"article":article })