from django.shortcuts import render, HttpResponse

# Create your views here.
def homePage(request):
    return HttpResponse("<h1>Welcome Home</h1>")