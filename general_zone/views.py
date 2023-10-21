from django.shortcuts import render
from django.http import HttpResponse
from  .models import contact_data
from  general_zone.models import contact_data
# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def comsignup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        organization = request.POST.get('organization')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword =request.POST.get('cpassword')
        if(password!=cpassword):
            return redirect('comsignup')
        if(len(phone)!=10 or len(phone)<10 or len(phone)>10):
            return redirect('comsignup')
        sign_up = User.objects.create_user(
            username=username,
            first_name=firstname,
            last_name=lastname,
            # organization=organization,
            # phone_number=phone,
            email=email,
            password=password,
        )
        sign_up.save()
        return redirect("comlogin")    
    return render(request,'com_signup.html')

def adminlogin(request):
    return render(request,'admin_login.html')

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

def trainer(req):
    return render(req,'trainers.html')

def con1(request):
    all_contacts = contact_data.objects.all()
    return render(request, 'adminpage.html', {'contacts': all_contacts})