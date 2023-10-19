from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
# Create your views here.

from django.http import HttpResponse
def cendashboard(request):
    return render(request,'cen_dashboard.html') 

def cenlogout(request):
    logout(request)
    # messages.success(request, 'You have been logged out successfully.')
    return  redirect('homepage')
def entrylogin(req):
    return render(req,'cen_entrylogin.html')