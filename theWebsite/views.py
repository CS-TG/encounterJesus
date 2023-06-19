from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def testimonies(request):
    return render(request, 'testimonies.html')