from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=100)
    address = models.TextField()
    contact_email = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    dob = models.DateField()


class DesignTemplate(models.Model):
    name = models.CharField(max_length=50)

class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    summary = models.TextField(null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    references = models.TextField(null=True, blank=True)
    template = models.ForeignKey(DesignTemplate, related_name='resumes', on_delete=models.CASCADE)


class Project(models.Model):
    user = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)    
    description = models.TextField(null=True, blank=True)


class Education(models.Model):
    user = models.ForeignKey(User, related_name='educations', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)  
    institute = models.CharField(max_length=100)  
    year_passed = models.SmallIntegerField()
    is_complete = models.BooleanField(default=True)