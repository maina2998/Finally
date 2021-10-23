from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt




# Create your views here.

@csrf_exempt
def login_user(request):  
    if request.method == "POST":        
        username = request.POST.get('username')       
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user) 
            return redirect('home:homepage.html')
         
    content = {}    
    return render(request,'base.html',content )

def log_out_user(request):    
    logout(request)   
    return redirect('login_user')
       

# def email(request):
#     subject = 'Thank you for registering to our site'
#     message = ' it  means a world to us '
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = ['receiver@gmail.com',]
#     send_mail( subject, message, email_from, recipient_list )
#     return redirect('redirect to a new page')      

# send_mail('Subject here', 'Here is the message.', 'from@example.com', ['to@example.com'], fail_silently=False)
