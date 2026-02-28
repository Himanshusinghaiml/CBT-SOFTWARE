from django.urls import path
from companylogin import views

urlpatterns=[
    path('com_dashboard/',views.com_dashboard,name="com_dashboard"),
    path('addexam/',views.addExam,name="addexam"),
    path('ongoingtests/',views.ongoing_tests,name="ongoingtests"),
    path('completedtests/',views.completed_tests,name="completedtests"),
    path('centers/',views.centers,name="centers"),
    path('addcenter/',views.addCenter,name="addcenter"),
    path('saveexam/',views.saveExam,name="saveexam"),
    path('logout/',views.comLogout,name="logout"),
    path('company-entry/',views.companyentry,name="companyentry"),
    path('password-center/',views.passcenter,name="passcenter"),
    path('questions/',views.questions,name="questions"),
    path('addquestion/',views.addQuestion,name="addquestion"),
    # AI-powered question generation
    path('generate-questions/', views.generate_questions, name='generate_questions'),
    path('questions/delete/<int:question_id>/', views.delete_question, name='delete_question'),
    path('centers/delete/<int:center_id>/', views.delete_center, name='delete_center'),
    path('tests/delete/<int:test_id>/', views.delete_test, name='delete_test'),
]