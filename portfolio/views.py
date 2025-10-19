from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Education, Certification, Experience, Project, Skill, ContactMessage

def home(request):
    context = {
        'profile': Profile.objects.first(),
        'education': Education.objects.all(),
        'certifications': Certification.objects.all(),
        'experience': Experience.objects.all(),
        'projects': Project.objects.filter(featured=True)[:3],
        'skills': Skill.objects.all(),
    }
    return render(request, 'portfolio/home.html', context)

def projects(request):
    context = {
        'profile': Profile.objects.first(),
        'projects': Project.objects.all(),
    }
    return render(request, 'portfolio/projects.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        messages.success(request, 'Message sent successfully! I will get back to you soon.')
        return redirect('contact')
    
    context = {
        'profile': Profile.objects.first(),
    }
    return render(request, 'portfolio/contact.html', context)
