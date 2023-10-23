from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.
def studhome(req):
    return render(req,'stud_home.html')
def instruction(req):
    return render(req,'instruction.html')

def running(req):
    start_time = datetime.now()
    end_time = start_time + timedelta(hours=1)  # Set the end time to 1 hour from now

    return render(req, 'running_exam.html', {
        'start_time': start_time.strftime("%Y-%m-%d %H:%M:%S"),  # Format the time as a string
        'end_time': end_time.strftime("%Y-%m-%d %H:%M:%S"),
    })
    # return render(req,'running_exam.html')