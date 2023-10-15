from django.urls import path
from general_zone import views

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('centerlogin/',views.centerlogin,name="centerlogin"),
    path('about/',views.about,name="about"),
    path( 'contact/',views.contact,name="contact"),
]