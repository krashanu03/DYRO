from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from resumes.models import Resume, UserProfile


from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
import datetime
from xhtml2pdf import pisa 


def home(request):
    return render(request, 'home.html')


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
    
    profile = UserProfile.objects.get(user=request.user)

    return render(request, 'resume-edit.html', {'resume': resume, 'profile': profile})


def resume_preview(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except:
        return HttpResponseRedirect(reverse('edit-profile'))

    return render(request, 'preview.html', {})


def profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except:
        user_profile = UserProfile(user=request.user)
        user_profile.save()

    return render(request, 'profile.html', {'profile': user_profile})


def edit_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except:
        user_profile = UserProfile(user=request.user, contact_email=request.user.email)
        user_profile.save()
    return render(request, 'edit-profile.html', {'profile': user_profile})


def save_profile(request):

    user_profile = UserProfile.objects.get(user=request.user)
    user_profile.father_name = request.POST['form_father_name']
    user_profile.contact_email = request.POST['form_email']
    user_profile.address = request.POST['form_address']
    user_profile.save()

    return HttpResponseRedirect(reverse('profile'))



def save_resume(request):
    resume = Resume.objects.get(user=request.user)
    resume.summary = request.POST['form_summary']
    resume.skills = request.POST['form_skills']
    resume.references = request.POST['form_references']

    resume.save()
    
    return HttpResponseRedirect(reverse('resume-preview'))


def generate_PDF(request):
    data = {'user':request.user}

    template = get_template('resume_template/%s.html' % request.user.resume.template_name)
    html  = template.render(data)

    file = open('resume.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,
            encoding='utf-8')

    file.seek(0)
    pdf = file.read()
    file.close()            
    return HttpResponse(pdf, 'application/pdf')    