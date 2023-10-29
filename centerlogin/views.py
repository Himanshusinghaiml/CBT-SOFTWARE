from django.shortcuts import render,redirect
from django.contrib import messages

from django.http import HttpResponse

def cendashboard(request):
    try:
        if request.session['center_id']:
            return render(request,'cen_dashboard.html')
    except KeyError:
        return redirect('centerlogin')  

def cenlogout(request):
    try:
        if request.session['center_id']:
            request.session['center_id'] = None
            messages.success(request, 'You have been logged out successfully.')
            return  redirect('centerlogin')
    except KeyError:
        pass
    return  redirect('centerlogin')

def entrylogin(request):
    try:
        if request.session['center_id']:
            return render(request,'cen_entrylogin.html')
    except KeyError:
        return redirect('centerlogin') 

def studentlist(request):
    try:
        if request.session['center_id']:
            return render(request,'studentlist.html')
    except KeyError:
        return redirect('centerlogin')

def  democenter(request):
    try:
        if request.session['center_id']:
            return render(request,'democenter.html')
    except KeyError:
        return redirect('centerlogin')

def  emergency(request):
    try:
        if request.session['center_id']:
            return render(request,'cen_emer.html')
    except KeyError:
        return redirect('centerlogin')

def  seatarr(request):
    try:
        if request.session['center_id']:
            return render(request,'seat_arrange.html')
    except KeyError:
        return redirect('centerlogin')
