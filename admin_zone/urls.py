from django.urls import path
from admin_zone import views

urlpatterns = [
    path('adminhome/',views.admin_home,name = "adminhome")
]