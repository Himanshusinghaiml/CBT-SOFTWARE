from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
 

# Create your views here.
def comsignup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        # organization = request.POST.get('organization')
        # phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # return  redirect('comlogin')
        sign_up = User.objects.create_user(
            username=username,
            first_name=firstname,
            last_name=lastname,
            # organization=organization,
            # phone_number=phone,
            email=email,
            password=password,
        )
        login(request, sign_up)
        sign_up.save()
        # return HttpResponse("successfully data saved in databse")
        return redirect("comlogin")
        
    return render(request,'com_signup.html')

def comlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return render(request, 'com_login.html')

    return render(request, 'com_login.html')

     


def comhomepage(request):
    return render(request,'com_homepage.html')

def comdashboard(request):
    return render(request,'com_dashboard.html')

def comlogout(request):
    content = """
    <html>
    <head>
        <title> CBT</title>
    </head>
    <body>
    <center>  <h1> Succesfully logout </h1></center>
         
         
        <center><a href="/">CLICK THE LINK AND REDIRECT THE HOME PAGE </a></center>
    </body>
    </html>
    """
    response = HttpResponse(content, content_type="text/html")
    return response
    # return HttpResponse("Successfully Log out <li><a href=" ">Home</a></li> ")