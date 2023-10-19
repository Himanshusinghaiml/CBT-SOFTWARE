from django.shortcuts import render

# Create your views here.
def studhome(req):
    return render(req,'stud_home.html')
def instruction(req):
    return render(req,'instruction.html')

def running(req):
    return render(req,'running_exam.html')