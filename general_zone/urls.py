from django.urls import path
from general_zone import views

urlpatterns = [
    path('',views.homepage,name="homepage"),
]