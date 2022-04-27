from  django.contrib import admin
from django.urls import path
from resumes import views

urlpatterns = [
 
    path('', views.resume_preview, name="home"),
    path('sign-up/', views.sign_up, name="sign-up"),
    path('resume-edit/', views.resume_edit, name="resume-edit"),
    path('resume-preview/', views.resume_preview, name="resume-preview"), # Download link from here.
    path('profile/', views.profile, name="profile")

]