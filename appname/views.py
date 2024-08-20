from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse


def webtoolsIndex(request):
    return render(request, 'portrait.html')