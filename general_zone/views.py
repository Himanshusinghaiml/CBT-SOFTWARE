from django.shortcuts import render
from django.http import HttpResponse
from  .models import contact_data
from  general_zone.models import contact_data
# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def centerlogin(request):
    return render(request,'centerlogin.html')

def about(request):
    return render(request,'about.html')

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
        message = message
    ) 
        contactdata.save()     
    return render(request,'contact.html')

def courses(request):
    return render(request,'courses.html')

def pricing(request):
    return render(request,'pricing.html')

def event(request):
    return render(request,'events.html')
def trainer(req):
    return render(req,'trainers.html')

def con1(request):
    all_contacts = contact_data.objects.all()
    return render(request, 'adminpage.html', {'contacts': all_contacts})