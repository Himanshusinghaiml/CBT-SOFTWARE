from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse
from django.contrib import messages

from .models import *
from companylogin.models import *
from admin_zone.models import *

def homepage(request):
    return render(request,'homepage.html')

def about(request):
    return render(request,'about.html')

def comsignup(request):
    if request.method == 'POST':
        username=request.POST.get('com_signup_name')
        phone = request.POST.get('com_signup_phone')
        email = request.POST.get('com_signup_email')
        password = request.POST.get('com_signup_password')
        company = Company(name=username, phone=phone, email=email, password=password)
        company.save()
        return JsonResponse({'success': True})     
    return JsonResponse({'success': False})  

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
        except Company.DoesNotExist:
            pass

    return redirect('homepage')

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
        except Center.DoesNotExist:
            pass

    return redirect('homepage')

def admin_login(request):
    try:
        if request.session['admin_id']:
            return redirect('adminhome')
    except KeyError:
        pass
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Admin.objects.get(email=email)
            if user.password == password:
                request.session['admin_id'] = user.id
                return redirect('adminhome')
        except Admin.DoesNotExist:
            pass

    return redirect('homepage')

def courses(request):
    return render(request,'courses.html')

def services(request):
    return render(request,'services.html')

def request_demo(request):
    if request.method=='POST':
        name = request.POST.get('contact_name')
        email = request.POST.get('contact_email')
        phone = request.POST.get('contact_phone')
        organization = request.POST.get('contact_organization')
        message = request.POST.get('contact_message')
        
        contactdata = contact_data(
        name = name,
        email = email,
        phone = phone,
        organization=organization,
        message = message ) 
        contactdata.save()
        return JsonResponse({'success': True})     
    return JsonResponse({'success': False})

def centerlist(request):
    centers = addnewCenterlist.objects.all()
    return render(request, 'centerlist.html', {'centers': centers})