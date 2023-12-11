from django.shortcuts import render,redirect
from django.core.exceptions import *
from .models import  *
from general_zone.models import *
from centerlogin.models import *
from companylogin.models import *
# from admin_zone.models import Center
# Create your views here.
def admin_home(request):
    try:
        user_id = request.session['admin_id']
        Admin_data = Admin.objects.get(id=user_id)
        all_contacts = contact_data.objects.all()
        Companys = Company.objects.all()
        Centers = Center.objects.all()
        Tests = Test.objects.all()

        return render(request, 'adminhome.html', {
            'contacts': all_contacts,
            'Companys': Companys,
            'Centers': Centers,
            'Tests': Tests,
            'Admin_data': Admin_data,
        })
    except (KeyError, ObjectDoesNotExist):
        return redirect('homepage')
    
def admin_logout(request):
    try:
        if request.session['admin_id']:
            request.session['admin_id'] = None
            return  redirect('homepage')
    except KeyError:
        pass
    return  redirect('homepage')

def add_center(request):
    if request.method=='POST':
        centercode = request.POST.get('centerCode')
        centername = request.POST.get('centerName')
        state = request.POST.get('state')
        place = request.POST.get('place')
        email = request.POST.get('emailId')
        contact = request.POST.get('contact')
        forsaving =addnewCenterlist(
        center_code = centercode,
        center_name = centername,
        state = state,
        place=place,
        email_id= email,
        contact=contact,  ) 
        forsaving.save()  
    return redirect ('adminhome')
    
    
