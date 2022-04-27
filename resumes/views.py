from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from resumes.models import UserProfile


def login (request):
    return render(request,'account/login.html')


def sign_up (request):
    return render(request,'index.html')


def resume_edit (request):
    return render(request,'resume-edit.html')


def resume_preview (request):
    return render(request,'preview.html')            


def profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except:
        user_profile = UserProfile(user=request.user)
        user_profile.save()

    return render(request, 'profile.html', {'profile': user_profile})


def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'edit-profile.html', {'profile': user_profile})


def save_profile(request):

    user_profile = UserProfile.objects.get(user=request.user)
    user_profile.father_name = request.POST['form_father_name']
    user_profile.contact_email = request.POST['form_email']
    user_profile.address = request.POST['form_address']
    user_profile.save()

    return HttpResponseRedirect(reverse('profile'))
    
    