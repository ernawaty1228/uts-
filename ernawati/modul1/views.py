from django.shortcuts import render
def index(request):
    return render(request, 'modul1/index.html')