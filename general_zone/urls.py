from django.urls import path
from general_zone import views

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('comsignup/',views.comsignup,name="comsignup"),
    path('centerlogin/',views.centerlogin,name="centerlogin"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('about/',views.about,name="about"),
    path( 'contact/',views.contact,name="contact"),
    path( 'trainers/',views.trainer,name="trainers"),
    path( 'courses/',views.courses,name="courses"),
    path( 'admin-control/',views.con1,name="adminpage"),
] 
 