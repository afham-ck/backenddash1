from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Course(models.Model):
    course_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
     



STATUS_CHOICES = [
    ('sem1', 'Sem1'),
    ('sem2', 'Sem2'),
    ('sem3', 'Sem3'),
    ('sem4', 'Sem4'),
    ('sem5', 'Sem5'),
    ('sem6', 'Sem6'),
]

class Sem(models.Model):
    sem_choice = models.CharField(max_length=10, choices=STATUS_CHOICES)
    
    def __str__(self):
        return self.get_sem_choice_display()  # returns the display value of the choice

    

  
    
class Subject(models.Model):   
    id = models.BigAutoField(primary_key=True)
    sub_id = models.CharField(max_length=10,unique=True)
    sub_name = models.CharField(max_length=10) 
    def __str__(self):
        return self.sub_name
    
    
class Qp(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=10,unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sem = models.ForeignKey(Sem, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE) 
    filepath = models.FileField(upload_to='pdfs/')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE) 
    upload_datetime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Videos(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sem = models.ForeignKey(Sem, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    filepath = models.FileField(upload_to='video/')
    upload_datetime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Studymaterials(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sem = models.ForeignKey(Sem, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    filepath = models.FileField(upload_to='pdfs/')
    upload_datetime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    
    
