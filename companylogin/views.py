from email import message
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.cache import never_cache
from django.views.decorators.cache import cache_control
from django.contrib import messages

# Create your views here.
 
def comlogin(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'com_login.html')

    return render(request, 'com_login.html')

    

@login_required(login_url='comlogin')
def comhomepage(request):
    return render(request,'com_homepage.html')

@login_required(login_url='comlogin')
def comdashboard(request):
    return render(request,'com_dashboard.html')

def addexam(request):
    return render(request,'add_exam.html')

@login_required
def comlogout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return  redirect('comlogin')
    