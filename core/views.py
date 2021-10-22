from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def login (request):
    if request.user.is_authenticated:
        data={}
        return render(request, "base.html", data)
    else:
        return redirect("auth_login")
       

 def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['receiver@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('redirect to a new page')      

send_mail('Subject here', 'Here is the message.', 'from@example.com', ['to@example.com'], fail_silently=False)
