from enum import unique
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.utils import timezone


class BaseUser(AbstractUser):
    username = None
    email = models.EmailField(unique= True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def is_panchayath(self): 
        if self.panchayath:
            return True
        else:
            return False

    
    def is_employee(self): 
        if self.employee:
            return True
        else:
            return False

class Panchayath(BaseUser):
    panchayath_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)


    def get_type(self):
        return 'panchayath'

    def __str__(self):
        return self.panchayath_name


class Employee(BaseUser): 
    panchayath_name = models.ForeignKey(Panchayath, on_delete= models.CASCADE, related_name='employee')  
    employee_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    address = models.TextField (default= '')
    phone = models.CharField(max_length=100, default = None)

    def get_type(self):
        return 'employee'

    def __str__(self):
        return self.employee_name


class EndUser(BaseUser):
    panchayath_name = models.ForeignKey(Panchayath, on_delete= models.CASCADE, related_name='enduser')  
    enduser_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    address = models.TextField (default= '')
    phone = models.CharField(max_length=100, default = None)


    def get_type(self):
        return 'enduser'

    def __str__(self):
        return self.enduser_name


class Complaint(models.Model):  
    panchayath_name = models.ForeignKey(Panchayath, on_delete= models.CASCADE, related_name='complaints')
    enduser = models.ForeignKey(EndUser,on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    solved = models.BooleanField(default=False)


class News(models.Model):
    panchayath_name = models.ForeignKey(Panchayath, on_delete= models.CASCADE, related_name='news')
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()


class Salary(models.Model):
    employee_name = models.ForeignKey(Employee, on_delete= models.CASCADE, related_name='salaries')
    panchayath_name = models.ForeignKey(Panchayath, on_delete= models.CASCADE, related_name='salaries')
    salary = models.IntegerField()
    ta = models.IntegerField()
    da = models.IntegerField()
    credited_on = models.DateTimeField(default=timezone.now)
    








