from django.db import models

class contact_data(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    organizations = models.CharField(max_length=200)
    message = models.TextField()

