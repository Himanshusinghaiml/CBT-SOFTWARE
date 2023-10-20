from django.urls import path
from companylogin import views

urlpatterns=[
    path('comlogin/',views.comlogin,name="comlogin"),
    path('comhomepage/',views.comhomepage,name="comhomepage"),
    path('dashboard/',views.comdashboard,name="dashboard"),
    path('addexam/',views.addexam,name="addexam"),
    path('logout/',views.comlogout,name="logout"),
]