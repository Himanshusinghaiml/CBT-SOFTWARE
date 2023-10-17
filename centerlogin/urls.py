from django.urls import path
from centerlogin import views
urlpatterns=[
    path('center-dashboard/',views.cendashboard,name="cendashboard"),
    path('center-logout/',views.cenlogout,name="cenlogout"),
]