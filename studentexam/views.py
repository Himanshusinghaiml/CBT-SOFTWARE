from django.shortcuts import render
from datetime import datetime, timedelta
from .models import Question # import table from models.py which will store question for all 

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
def over(req):
    return render(req,'submit.html')

new_question = Question(
    question_text="what is your  rally laptop name ?",
    option1="monkey",
    option2="asus",
    option3="jp",
    option4="hp",
    correct_option="option1"
)
existing_question = Question.objects.filter(question_text=new_question.question_text).first()

if not existing_question:
    # Save the new question to the database only if it doesn't already exist
    new_question.save()

# this is for exam conducting exam using ajax technology 
from django.http import JsonResponse
from .models import Question

def get_next_question(request, current_question_id):
    try:
        next_question = Question.objects.get(id=current_question_id + 1)
    except Question.DoesNotExist:
        next_question = None
    
    if next_question:
        data = {
            'question_text': next_question.question_text,
            'option1': next_question.option1,
            'option2': next_question.option2,
            'option3': next_question.option3,
            'option4': next_question.option4,
        }
    else:
        data = {
            'question_text': "No more questions",
            'option1': '',
            'option2': '',
            'option3': '',
            'option4': '',
        }

    return JsonResponse(data)

def get_previous_question(request, current_question_id):
    if current_question_id > 1:
        previous_question = Question.objects.get(id=current_question_id - 1)
    else:
        previous_question = None

    if previous_question:
        data = {
            'question_text': previous_question.question_text,
            'option1': previous_question.option1,
            'option2': previous_question.option2,
            'option3': previous_question.option3,
            'option4': previous_question.option4,
        }
    else:
        data = {
            'question_text': "No previous questions",
            'option1': '',
            'option2': '',
            'option3': '',
            'option4': '',
        }

    return JsonResponse(data)
