from django.shortcuts import render

# Create your views here.

def articles_list(request):
    return render(request, 'articles/article_list.html')

def hey(request):
    return render(request, 'articles/hey.html')