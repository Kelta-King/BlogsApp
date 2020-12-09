from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    
    #return HttpResponse("Home page")
    return render(request, "homePage.html")
    
    
def aboutPage(request):
    
    #return HttpResponse("About page")
    return render(request, "aboutPage.html")