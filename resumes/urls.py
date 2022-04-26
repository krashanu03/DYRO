from  django.contrib import admin
from django.urls import path
from resumes import views

urlpatterns =[
 
    path('',views.index,name="resumes")

]