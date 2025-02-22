from django.db import models
from django.contrib.auth.models import AbstractUser

class Teacher(AbstractUser):
    pass

# Student Model
class Student(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()

    class Meta:
        db_table = "Student"
