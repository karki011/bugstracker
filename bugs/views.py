from django.shortcuts import render
# Create your views here.


def home(request):
    html = 'bugs/home.html'
    return render(request, html)