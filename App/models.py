from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=40, null=True)
    semester=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    phone=models.IntegerField()
    batch=models.CharField(max_length=10)

def __str__(self):
    return self.name
