from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def flower(request):
    return render(request, 'flower.html')