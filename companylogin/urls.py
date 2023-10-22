from django.urls import path
from companylogin import views

urlpatterns=[
    path('comlogin/',views.comlogin,name="comlogin"),
    path('comhomepage/',views.comhomepage,name="comhomepage"),
    path('dashboard/',views.comdashboard,name="dashboard"),
    path('addexam/',views.addexam,name="addexam"),
    path('ongoingtests/',views.ongoing_tests,name="ongoingtests"),
    path('completedtests/',views.completed_tests,name="completedtests"),
    path('centers/',views.centers,name="centers"),
    path('addcenter/',views.addcenter,name="addcenter"),
    path('saveexam/',views.saveexam,name="saveexam"),
    path('logout/',views.comlogout,name="logout"),
    path('company-entry/',views.companyentry,name="companyentry"),
    path('password-center/',views.passcenter,name="passcenter"),
]