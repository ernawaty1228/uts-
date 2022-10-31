#from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
    return render(request,'index.html')


# method view index
#def index(request):
    #return HttpResponse("<h1> ini adalah home</h1>")