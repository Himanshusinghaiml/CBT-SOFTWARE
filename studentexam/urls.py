from django.urls import path
from studentexam import views
urlpatterns=[
    path('student-home/',views.studhome,name="studhome"),
    path('instruction/',views.instruction,name="instruction"),
    path('running-exam/',views.running,name="running"),
    path('over/',views.over,name="over"),
]