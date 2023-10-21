from django.urls import path
from general_zone import views

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('comsignup/',views.comsignup,name="comsignup"),
    path('centerlogin/',views.centerlogin,name="centerlogin"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('about/',views.about,name="about"),
<<<<<<< HEAD
    path( 'contact/',views.contact,name="contact"),
    path( 'pricing/',views.pricing,name="pricing"),
    path( 'events/',views.event,name="events"),
    path( 'trainers/',views.trainer,name="trainers"),
    path( 'courses/',views.courses,name="courses"),
    path( 'admin-control/',views.con1,name="adminpage"),
] 
=======
    path('contact/',views.contact,name="contact"),
    path('trainers/',views.trainer,name="trainers"),
    path('courses/',views.courses,name="courses"),
]
>>>>>>> 1f016fc449c5b9497ebac4bbfdb827d8ec846c82
