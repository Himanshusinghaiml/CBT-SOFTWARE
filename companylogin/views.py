from django.shortcuts import render

# Create your views here.
def company(request):
    return render(request,'com_signup.html')

def comlogin(request):
    return render(request,'com_login.html')

def comhomepage(request):
    return render(request,'com_homepage.html')