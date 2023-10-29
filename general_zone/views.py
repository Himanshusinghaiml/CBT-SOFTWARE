from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from  .models import *
from  companylogin.models import *

def homepage(request):
    return render(request,'homepage.html')

def about(request):
    return render(request,'about.html')

def comsignup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword =request.POST.get('cpassword')
        if Company.objects.filter(email=email).exists():
            messages.error(request,'Email already exist. please try with another email !')
            return redirect('comsignup')
        if(password!=cpassword):
            messages.error(request,'Password and confirm password should be same !')
            return redirect('comsignup')
        if(len(phone)!=10):
            messages.error(request,'Mobile number should be 10 digit long !')
            return redirect('comsignup')

        company = Company(name=username, phone=phone, email=email, password=password)
        company.save()
        messages.success(request, 'Your account is created successfully. Please log in.')
        return redirect("comlogin")    
    return render(request,'com_signup.html')

def comLogin(request):
    try:
        if request.session['com_id']:
            return redirect('com_dashboard')
    except KeyError:
        pass
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Company.objects.get(email=email)
            if user.password == password:
                request.session['com_id'] = user.id
                return redirect('com_dashboard')
            else:
                messages.error(request, 'Incorrect password ❌ Please try again.')
        except Company.DoesNotExist:
            messages.error(request, 'User not found ❌ Please Sign up before Sign in.')

    return render(request, 'com_login.html')

def centerlogin(request):
    try:
        if request.session['center_id']:
            return redirect('entrylogin')
    except KeyError:
        pass
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Center.objects.get(email=email)
            if user.password == password:
                request.session['center_id'] = user.id
                return redirect('entrylogin')
            else:
                messages.error(request, 'Incorrect password ❌ Please try again.')
        except Center.DoesNotExist:
            messages.error(request, 'User not found ❌ Please contact your organization.')

    return render(request, 'centerlogin.html')

def adminlogin(request):
    return render(request,'admin_login.html')

def courses(request):
    return render(request,'courses.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        organizations = request.POST.get('organizations')
        message = request.POST.get('message')
        
        contactdata = contact_data(
        name = name,
        email = email,
        phone = phone,
        organizations=organizations,
        message = message ) 
        contactdata.save() 
        messages.success(request,'Sucessfully submitted.Our Executive will reach you soon. Thank you .🤗 ')    
    return render(request,'contact.html')

def con1(request):
    all_contacts = contact_data.objects.all()
    return render(request, 'adminpage.html', {'contacts': all_contacts})

def requestdemo(request):
    return render(request,'request_demo.html')
