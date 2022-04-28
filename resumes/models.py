from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    father_name = models.CharField(max_length=100)
    address = models.TextField()
    contact_email = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)


class DesignTemplate(models.Model):
    name = models.CharField(max_length=50)

class Resume(models.Model):
    user = models.OneToOneField(User, related_name='resume', on_delete=models.CASCADE)
    summary = models.TextField(null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    references = models.TextField(null=True, blank=True)
    template_name = models.CharField(max_length=50, default='default') #models.ForeignKey(DesignTemplate, related_name='resumes', on_delete=models.CASCADE)


class Experience(models.Model):
    user = models.ForeignKey(User, related_name='experiences', on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)    
    org_name = models.CharField(max_length=100)    
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=100)    
    responsebilities = models.TextField(null=True, blank=True)


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