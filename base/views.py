from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request, 'base/index.html')

def about(request):
    return render(request, 'base/about.html')
