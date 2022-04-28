from  django.contrib import admin
from django.urls import path
from resumes import views

urlpatterns = [
 
    path('', views.resume_preview, name="home"),
    path('sign-up/', views.sign_up, name="sign-up"),
    path('resume-edit/', views.resume_edit, name="resume-edit"),
    path('resume-preview/', views.resume_preview, name="resume-preview"), # Download link from here.
    path('profile/', views.profile, name="profile"),
    path('edit-profile/', views.edit_profile, name="edit-profile"),
    path('save-profile/', views.save_profile, name="save-profile"),
    path('save-resume/', views.save_resume, name="save-resume"),
    path('resume-pdf/', views.generate_PDF, name="resume-pdf"),

]