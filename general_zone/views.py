from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request,'contact.html')

def courses(request):
    return render(request,'courses.html')

def services(req):
    return render(req,'services.html')

def requestdemo(req):
    return render(req,'request_demo.html')