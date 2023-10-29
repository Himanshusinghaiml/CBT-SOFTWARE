from django.urls import path
from general_zone import views

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('comsignup/',views.comsignup,name="comsignup"),
    path('comlogin/',views.comLogin,name="comlogin"),
    path('centerlogin/',views.centerlogin,name="centerlogin"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('services/',views.services,name="services"),
    path('courses/',views.courses,name="courses"),
    path('requestdemo/',views.requestdemo,name="requestdemo"),
    path( 'admin-control/',views.con1,name="adminpage"),
]
