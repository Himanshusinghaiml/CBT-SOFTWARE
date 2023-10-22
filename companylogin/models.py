from django.db import models

class Tests(models.Model):
    test_name = models.CharField(max_length=128)
    no_of_questions = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField()
    status = models.CharField(max_length=128,default="Active")
    
class Centers(models.Model):
    center_name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    profile_pic = models.FileField(upload_to='profile_pic/',null=True,default=None)
    password = models.CharField(max_length=128)