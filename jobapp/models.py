from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class MyUserModel(AbstractUser):
    phone = models.CharField(max_length=12)
    options=(("Male","Male"),
             ("Female","Female"),
             ("Others","Others"))
    gender = models.CharField(max_length=25,choices=options)
    option=(("job seeker","job seeker"),
            ("Employer","Employer"))
    role=models.CharField(max_length=25,choices=option,default="job seeker")

class UserProfileModel(models.Model):
    user=models.OneToOneField(MyUserModel,on_delete=models.CASCADE)
    qualification=models.CharField(max_length=20)
    skills=models.CharField(max_length=250)
    experience=models.FloatField()

class EmployerProfileModel(models.Model):
    company_name=models.OneToOneField(MyUserModel,on_delete=models.CASCADE)
    location=models.CharField(max_length=100)


class Job(models.Model):
    job_title = models.CharField(max_length=30)
    employer=models.ForeignKey(EmployerProfileModel,on_delete=models.CASCADE)
    job_details=models.CharField(max_length=100)
    options=(("Active","Active"),
             ("Closed","Closed"))
    status=models.CharField(max_length=25,choices=options,default="Active")
    date_created=models.DateField(auto_now=True)
    last_date=models.DateField()

class Application(models.Model):
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    job_seeker=models.CharField(max_length=100)
    options=(("Viewed","Viewed"),
             ("Rejected","Rejected"),
             ("OnReview","OnReview"),
             ("Submitted","Submitted"))
    status=models.CharField(max_length=25,choices=options,default="Submitted")

