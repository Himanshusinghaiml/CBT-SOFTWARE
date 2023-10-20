from django.urls import path
from centerlogin import views
urlpatterns=[
    path('center-dashboard/',views.cendashboard,name="cendashboard"),
    path('center-logout/',views.cenlogout,name="cenlogout"),
    path('center-entry-login/',views.entrylogin,name="entrylogin"),
    path('student-list/',views.studentlist,name="studentlist"),
    path('demo-center/',views. democenter,name="democenter"),
    path('cent-eremergency/',views. emergency,name="emergency"),
    path('cent-erarrange/',views.seatarr,name="arrange"),
]