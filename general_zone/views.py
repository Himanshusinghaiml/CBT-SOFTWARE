from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def centerlogin(request):
    return render(request,'centerlogin.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')