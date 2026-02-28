from email import message
from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import *
from general_zone.models import *
from admin_zone.models import *
from centerlogin.models import *

# optional OpenAI integration for auto question generation
import os
from django.conf import settings
try:
    import openai
except ImportError:
    openai = None
from django.contrib.auth.hashers import make_password


def com_dashboard(request):
    try:
        if request.session['com_id']:
            user_id = request.session.get('com_id')
            Company_data = Company.objects.get(id = user_id)
            return render(request,'com_dashboard.html',{'Company_data':Company_data})
    except KeyError:
        pass
    return redirect('homepage')

def comLogout(request):
    try:
        if request.session['com_id']:
            request.session['com_id'] = None
    except KeyError:
        pass
    return  redirect('homepage')

def addExam(request):
    try:
        if request.session['com_id']:
            return render(request,'add_exam.html')
    except KeyError:
        pass
    return redirect('homepage') 
   
def saveExam(request):
    try:
        if request.session['com_id']:
            if request.method=='POST': 
                name = request.POST.get('exam_name') 
                no = request.POST.get('no_of_questions')  
                marks = request.POST.get('total_marks')  
                exam = Test(test_name = name,no_of_questions=no,total_marks=marks) 
                exam.save()    
                return redirect('com_dashboard')
    except KeyError:
        pass
    return redirect('homepage') 

def ongoing_tests(request):
    try:
        if request.session['com_id']:
            tests = Test.objects.all()
            return render(request,'ongoing_tests.html',{'tests':tests})
    except KeyError:
        pass
    return redirect('homepage') 
    
def completed_tests(request):
    try:
        if request.session['com_id']:
            tests = Test.objects.all()
            return render(request,'completed_tests.html',{'tests':tests})
    except KeyError:
        pass
    return redirect('homepage') 

def centers(request):
    try:
        if request.session['com_id']:
            centers = Center.objects.all()
            return render(request,'centers.html',{'centers':centers})
    except KeyError:
        pass
    return redirect('homepage') 
    
def addCenter(request):
    try:
        if request.session['com_id']:
            if request.method=='POST':
                center_name = request.POST.get('center_name')
                address = request.POST.get('address')
                phone = request.POST.get('phone')
                email = request.POST.get('email')
                profile_pic = request.POST.get('profile_pic')
                password = request.POST.get('password')
                from django.contrib.auth.hashers import make_password
                center = Center(center_name=center_name,address=address,phone=phone,email=email,profile_pic=profile_pic,password=make_password(password))
                center.save()
            return redirect('centers')
    except KeyError:
        pass
    return redirect('homepage') 

def questions(request):
    try:
        if request.session['com_id']:
            # allow simple filtering by topic/difficulty using query params
            questions = Question.objects.all()
            topic = request.GET.get('topic')
            if topic:
                questions = questions.filter(topic__icontains=topic)
            difficulty = request.GET.get('difficulty')
            if difficulty:
                questions = questions.filter(difficulty__icontains=difficulty)
            return render(request,'questions.html',{ 'questions':questions})
    except KeyError:
        pass
    return redirect('homepage') 
 
def addQuestion(request):
    try:
        if request.session['com_id']:
            if request.method=='POST':
                question = request.POST.get('question')
                option_1 = request.POST.get('option_1')
                option_2 = request.POST.get('option_2')
                option_3 = request.POST.get('option_3')
                option_4 = request.POST.get('option_4')
                correct_option = request.POST.get('correct_option')
                marks = request.POST.get('marks')
                # topic, difficulty may be provided by future forms
                topic = request.POST.get('topic', '')
                difficulty = request.POST.get('difficulty', '')
                question = Question(question=question,
                                     option_1=option_1,
                                     option_2=option_2,
                                     option_3=option_3,
                                     option_4=option_4,
                                     correct_option=correct_option,
                                     marks=marks,
                                     topic=topic,
                                     difficulty=difficulty,
                                     generated_by='manual')
                question.save()
            return redirect('questions')
    except KeyError:
        pass
    return redirect('homepage') 


def delete_question(request, question_id):
    """Remove a question by id and redirect back to list."""
    try:
        if request.session.get('com_id'):
            Question.objects.filter(id=question_id).delete()
    except KeyError:
        pass
    return redirect('questions')


def generate_questions(request):
    """Generate multiple choice questions using an AI model and save them.

    The POST body should contain 'topic' and optionally 'count' and
    'difficulty'.  The view returns JSON with a success flag and the number
    of questions added.
    """
    if request.method != 'POST':
        return HttpResponse(status=405)

    if not request.session.get('com_id'):
        return HttpResponse(status=403)

    topic = request.POST.get('topic', '').strip()
    try:
        count = int(request.POST.get('count', 5))
    except ValueError:
        count = 5
    difficulty = request.POST.get('difficulty', '').strip()

    added = 0
    if topic and openai:
        for q in generate_questions_from_ai(topic, count, difficulty):
            # basic validation
            opts = q.get('options', [])
            if len(opts) < 4:
                continue
            Question.objects.create(
                question=q.get('question', ''),
                option_1=opts[0],
                option_2=opts[1],
                option_3=opts[2],
                option_4=opts[3],
                correct_option=q.get('answer', ''),
                marks=q.get('marks', 1),
                topic=topic,
                difficulty=difficulty,
                generated_by='ai',
            )
            added += 1

    # after creation redirect back to list so admin sees new questions
    return redirect('questions')


def generate_questions_from_ai(topic, count=5, difficulty=None):
    """Simple wrapper around OpenAI API that yields question dicts.

    The returned list has entries like {
        'question': str,
        'options': [opt1, opt2, opt3, opt4],
        'answer': str,
        'marks': int,
    }
    """
    results = []
    if openai is None:
        return results

    # ensure api key is configured
    key = getattr(settings, 'OPENAI_API_KEY', None) or os.environ.get('OPENAI_API_KEY')
    if not key:
        return results
    openai.api_key = key

    prompt = (
        f"Generate {count} multiple choice questions on the topic '{topic}'"
    )
    if difficulty:
        prompt += f" with {difficulty} difficulty"
    prompt += ". Provide each question followed by four options labeled A,B,C,D and indicate the correct letter."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000,
            temperature=0.7,
        )
        text = response.choices[0].message.content
    except Exception:
        text = ""

    # naive parsing: split by lines and interpret
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    current = {}
    for line in lines:
        if line.lower().startswith('1.') or line[0].isdigit() and line[1] == '.':
            # new question
            if current:
                results.append(current)
            current = {'question': line.split('.',1)[1].strip(), 'options': [], 'answer': '', 'marks': 1}
        elif line.startswith('A.') or line.startswith('a.'):
            current['options'].append(line.split('.',1)[1].strip())
        elif line.startswith('B.') or line.startswith('b.'):
            current['options'].append(line.split('.',1)[1].strip())
        elif line.startswith('C.') or line.startswith('c.'):
            current['options'].append(line.split('.',1)[1].strip())
        elif line.startswith('D.') or line.startswith('d.'):
            current['options'].append(line.split('.',1)[1].strip())
        elif line.lower().startswith('answer:') or line.lower().startswith('correct'):
            # extract letter or option
            ans = line.split(':',1)[1].strip()
            current['answer'] = ans
    if current:
        results.append(current)
    return results

def delete_center(request, center_id):
    """Remove a center by id and redirect back to centers list."""
    try:
        if request.session.get('com_id'):
            Center.objects.filter(id=center_id).delete()
    except KeyError:
        pass
    return redirect('centers')


def delete_test(request, test_id):
    """Remove a test by id and redirect back to the appropriate list."""
    try:
        if request.session.get('com_id'):
            test = Test.objects.filter(id=test_id).first()
            if test:
                source = 'completedtests' if test.status == 'Completed' else 'ongoingtests'
                test.delete()
                return redirect(source)
    except KeyError:
        pass
    return redirect('ongoingtests')


def companyentry(request):
    try:
        if request.session['com_id']:
            return render(request,'com_entry.html')
    except KeyError:
        pass
    return redirect('homepage') 

def passcenter(request):
    try:
        if request.session['com_id']:
            return render(request,'pass_center.html')
    except KeyError:
        pass
    return redirect('homepage') 

