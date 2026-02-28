# CBT-SOFTWARE
# How To Run
------------------------------------------------------------------------
- Install dependency with `pip install -r requirements.txt`
- run django make migrations `python manage.py makemigrations`
- run django migrations `python manage.py migrations`
    **IMPORTANT:** after updating the code you will need new migrations for
    the extended `Question` model, e.g. `python manage.py makemigrations companylogin`.
- create django superuser with `python manage.py createsuperuser`
- run django server with `python manage.py runserver`
- Test the API as follows

- Sign up the user with `signup` API first and get the token
- [Online Examination System](https://www.linkedin.com/in/akashanand6353/)implemented as the final project for my Computer Engineering Bachelor's Degree.

## Table of Content
* [Demo](#demo)
* [Features](#features)
* [Built Using](#built-using)
* [Design Inspiration](#design-inspo)
* [Feedback](#feedback)
* [Author](#author)



## <a name="demo"></a>  Demo
![Game Demo](assets/images/demo.gif)

## <a name="features"></a>  Features
* ### General Features
    - Cross-platform
    - Responsive7
    - Accessible
    - Supports objective questions

        
* ### User-specific features
    * #### Student
        
        - Resumption capability for students
        - Automatic grading
        - Question randomization
        - AI based software (auto‑generated questions & metadata)
    * #### Examiner
        
        - Manage exams and set questions for assigned courses.
        - Activate exams.
        - Set exam time and instruction.
        - View all exam results of exams for assigned courses.
        
    * #### Administrator
        
        - Register users and courses.
        - View users and courses.
        - Modify and delete users/courses (TODO)


<br>

## <a name="built-using"></a> Built Using:
- HTML
- CSS
- JavaScript
- Bootstrap
- Django
- SQLite3
- mysql 

## AI Features
This project now integrates with the OpenAI API to automatically create
multiple choice questions.  To use this feature you must set an
`OPENAI_API_KEY` environment variable (or add it to `CBT/settings.py`).
Company users can click "Auto Generate" on the questions page and provide a
topic, number of questions and optional difficulty; the system will call the
AI model, save the results and make them available to students.

The generated questions are tagged with `generated_by='ai'` and the topic/
difficulty are stored for later filtering.

Feel free to extend the helper in `companylogin/views.py` if you want a
different prompt or output format.

## <a name="design-inspo"></a> Design Inspiration
The backend interface of this project was inspired by [Himanshu singh, Akash Anand] 

## <a name="feedback"></a> Feedback
Any questions or suggestions? Notice any bugs or glitches? Feel free to send me on [email](himanshusingh945443@gmail.com) and (9765akashanand@gmail.com)

## <a name="author"></a> Author 
