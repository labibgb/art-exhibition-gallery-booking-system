from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import feedback
from django.contrib import messages
# Create your views here.
def Feedback(request):
    if request.method == 'POST':
        subject = 'User feedback'
        email = request.POST['email']
        message = request.POST['message']
        email_from = settings.EMAIL_HOST_USER
        fd = feedback( email=email , message=message) 
        fd.save()
        recipient_list = ['labibgb@gmail.com',]
        send_mail( subject, message, email_from, recipient_list )
        messages.success( request , "Feedback send successfull.")
        return redirect('/')
    return redirect('/')
    