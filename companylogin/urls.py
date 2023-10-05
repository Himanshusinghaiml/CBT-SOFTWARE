from django.urls import path
from companylogin import views
urlpatterns=[
    path('companylogin/',views.company,name="companylogin"),
]