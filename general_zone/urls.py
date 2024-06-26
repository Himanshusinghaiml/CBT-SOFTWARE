from django.urls import include, path
from general_zone import views
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet


router = DefaultRouter()
router.register(r'company', CompanyViewSet, basename='company')

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('comsignup/',views.comsignup,name="comsignup"),
    path('comlogin/',views.comLogin,name="comlogin"),
    path('centerlogin/',views.centerlogin,name="centerlogin"),
    path('adminlogin/',views.admin_login,name="adminlogin"),
    path('about/',views.about,name="about"),
    path('services/',views.services,name="services"),
    path('courses/',views.courses,name="courses"),  
    path( 'homepage-centerlist/',views.centerlist,name="centerlist"),
    path('requestdemo/',views.request_demo,name="requestdemo"),

    
    path('', include(router.urls)),

]
