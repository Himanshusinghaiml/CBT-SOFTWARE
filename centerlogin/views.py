from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def c(request):
    return render(request,'c.html') 
