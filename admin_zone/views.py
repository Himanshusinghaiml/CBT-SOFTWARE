from django.shortcuts import render
from .models import  *
from general_zone.models import *
from centerlogin.models import *
from companylogin.models import *
# Create your views here.
def admin_home(request):
    all_contacts = contact_data.objects.all()
    Companys = Company.objects.all()
    Centers = Center.objects.all()
    Tests = Test.objects.all()
    return render(request, 'adminhome.html',{
        'contacts': all_contacts,
        'Companys':Companys,
        'Centers':Centers,
        'Tests':Tests
    })
    
