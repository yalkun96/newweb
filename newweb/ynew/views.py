from django.db.models import QuerySet
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template.loader import get_template
from django.core import *
from django.db import models

from .forms import *
from .models import *
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives

from .models import Video


def home(request):
    tasks = Info.objects.all()
    video = Video.objects.all()
    return render(request, 'ynew/home.html', {'video': video, 'tasks': tasks})

def video(request):
    video = Video.objects.all()
    return render(request, 'ynew/test.html', {'video': video})

def about(request):
    task = Info.objects.all()
    return render(request, 'ynew/about.html', {'task': task})

def my_works(request):
    video = Video.objects.all()
    return render(request, 'ynew/portfolio.html', {'video': video})

def contact(request):
    task = Info.objects.all()
    contacts = ContactInfo.objects.all()
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message'])
            messages.success(request, 'Thank you!')
            form = ContactForm()

    else:
        form = ContactForm()

    return render(request, 'ynew/contact.html', {'form': form, 'context': context, 'contacts': contacts, 'task': task})



def send_message(name, email, message):
    text = get_template('ynew/message.html')
    html = get_template('ynew/message.html')
    context = {'name': name, 'e-mail': email, 'message': message}
    subject = "Message from user"
    from_email = 'from@example.com'
    text_content = text.render(context)
    html_content = text.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['manager@example.com'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
