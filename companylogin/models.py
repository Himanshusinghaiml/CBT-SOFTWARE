from django.db import models

class Tests(models.Model):
    test_name = models.CharField(max_length=128)
    no_of_questions = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField()
    status = models.CharField(max_length=128,default="Active")

    