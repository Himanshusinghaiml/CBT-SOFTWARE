from django.shortcuts import render,redirect
from django.contrib import messages

from django.http import HttpResponse

def cendashboard(request):
    try:
        if request.session['center_id']:
            return render(request,'cen_dashboard.html')
    except KeyError:
        pass
        return redirect('homepage')  

def cenlogout(request):
    try:
        if request.session['center_id']:
            request.session['center_id'] = None
            return  redirect('homepage')
    except KeyError:
        pass
    return  redirect('homepage')

def entrylogin(request):
    try:
        if request.session['center_id']:
            return render(request,'cen_entrylogin.html')
    except KeyError:
        pass
    return redirect('homepage')

def studentlist(request):
    try:
        if request.session['center_id']:
            return render(request,'studentlist.html')
    except KeyError:
        pass
    return redirect('homepage')

def democenter(request):
    try:
        if request.session['center_id']:
            return render(request,'democenter.html')
    except KeyError:
        pass
    return redirect('homepage')

def emergency(request):
    try:
        if request.session['center_id']:
            return render(request,'cen_emer.html')
    except KeyError:
        pass
    return redirect('homepage')

def seatarr(request):
    try:
        if request.session['center_id']:
            return render(request,'seat_arrange.html')
    except KeyError:
        pass
    return redirect('homepage')
