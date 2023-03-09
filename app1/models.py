from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Employee(models.Model):
    # status_choices = [
    #     ('Male'),
    #     ('Female'),
    # ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10) #choices=status_choices
    email = models.EmailField()
    department = models.CharField(max_length=500)
    company_name = models.CharField(max_length=500)
    leave_available = models.CharField(max_length=500, null=True)

class holiday(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=500)

class Employee_leave(models.Model):
    date = models.DateField()
    reason = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)





