from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from resumes.models import UserProfile
from resumes.models import Resume


def login(request):
    return render(request, 'account/login.html')


def sign_up(request):
    return render(request, 'index.html')


def resume_edit(request):
    try:
        resume = Resume.objects.get(user=request.user)
    except:
        resume = Resume(user=request.user)
        resume.save()
    return render(request, 'resume-edit.html', {'resume-edit': Resume})


def resume_preview(request):
    resume = Resume.objects.get(user=request.user)
    return render(request, 'preview.html', {'preview': Resume})


def save_resume(request):

    resume = Resume.objects.get(user=request.user)
    resume.summary = request.POST['form_summary']
    resume.skills = request.POST['form_skills']
    resume.references = request.POST['form_references']
    resume.experience = request.POST['form_experience']
    resume.education = request.POST['form_education']
    resume.personal_details = request.POST['form_personal_details']
    resume.save()

    return HttpResponseRedirect(reverse('resume-edit'))


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
