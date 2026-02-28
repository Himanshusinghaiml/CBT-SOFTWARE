from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse
from django.contrib import messages

from general_zone.serializers import CompanySerializer

from .models import *
from companylogin.models import *
from admin_zone.models import *

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
# from .models import Company
from .serializers import CompanySerializer
from django.contrib.auth.hashers import make_password, check_password

def homepage(request):
    return render(request,'homepage.html')

def about(request):
    return render(request,'about.html')

# Django restframework viewsets 

class CompanyViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def signup(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True})
        return Response({'success': False, 'errors': serializer.errors})
    
    @action(detail=False, methods=['post'])
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            company = Company.objects.get(email=email, password=password)
            return Response({'success': True, 'company': CompanySerializer(company).data})
        except Company.DoesNotExist:
            return Response({'success': False, 'error': 'Invalid email or password'})


def comsignup(request):
    if request.method == 'POST':
        name=request.POST.get('com_signup_name')
        phone = request.POST.get('com_signup_phone')
        email = request.POST.get('com_signup_email')
        password = request.POST.get('com_signup_password')
        if Company.objects.filter(email=email).exists():
            return render(request, 'homepage', {'error': 'Email already exists'})
        # store hashed password
        company = Company(name=name, phone=phone, email=email, password=make_password(password))
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
            if check_password(password, user.password):
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
            if check_password(password, user.password):
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
            if check_password(password, user.password):
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