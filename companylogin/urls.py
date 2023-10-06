from django.urls import path
from companylogin import views
urlpatterns=[
    path('companyzone/',views.company,name="companyzone"),
    path('comlogin/',views.comlogin,name="comlogin"),
    path('comhomepage/',views.comhomepage,name="comhomepage"),
]