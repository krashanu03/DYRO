from django.shortcuts import render

def login (request):
    return render(request,'account/login.html')


def sign_up (request):
    return render(request,'index.html')


def resume_edit (request):
    return render(request,'index.html')


def resume_preview (request):
    return render(request,'preview.html')            