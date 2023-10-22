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
from .models import *

# Create your views here.
 
def comlogin(request):
    if request.user.is_authenticated:
        return redirect('companyentry')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('companyentry')
        else:
            messages.error(request,' Invalid Credientials ❌ try again !')
            return render(request, 'com_login.html')

    return render(request, 'com_login.html')

    
def saveexam(request):
    result=""
    if request.method=='POST': 
        name = request.POST.get('exam_name') 
        no = request.POST.get('no_of_questions')  
        marks = request.POST.get('total_marks')  
        exam = Tests(test_name = name,no_of_questions=no,total_marks=marks) 
        exam.save()    
    return redirect('dashboard')

def ongoing_tests(request):
    tests = Tests.objects.all()
    return render(request,'ongoing_tests.html',{'tests':tests})

def completed_tests(request):
    tests = Tests.objects.all()
    return render(request,'completed_tests.html',{'tests':tests})

def centers(request):
    centers = Centers.objects.all()
    return render(request,'centers.html',{'centers':centers})

def addcenter(request):
    msg=""
    if request.method=='POST':
        center_name = request.POST.get('center_name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        profile_pic = request.POST.get('profile_pic')
        password = request.POST.get('password')
        center = Centers(center_name=center_name,address=address,phone=phone,email=email,profile_pic=profile_pic,password=password)
        center.save()
        messages.success(request, 'Center data added successfully.')
    return render(request,'centers.html')

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
def companyentry(req):
    return render(req,'com_entry.html')

def passcenter(req):
    return render(req,'pass_center.html')