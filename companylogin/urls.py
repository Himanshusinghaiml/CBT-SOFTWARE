from django.urls import path
from companylogin import views

urlpatterns=[
    path('comsignup/',views.comsignup,name="comsignup"),
    path('comlogin/',views.comlogin,name="comlogin"),
    path('comhomepage/',views.comhomepage,name="homepage"),
    path('dashboard/',views.comdashboard,name="dashboard"),
    path('logout/',views.comlogout,name="logout"),
]