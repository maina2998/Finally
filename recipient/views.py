from django.shortcuts import render,redirect
from recipient.models import Recipient
from .models import Recipient
from .forms import RecipientRegistrationForm
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def register_recipient(request):
    if request.method=="POST":
        form=RecipientRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=RecipientRegistrationForm()
        
    return render(request,"register_recipient.html",{"form":form})

def recipient_list(request):
    recipients=Recipient.objects.all()
    return render(request,"recipient_list.html",{"recipients":recipients})

def recipient_profile(request,id):
    recipient=Recipient.objects.get(id=id)
    return render(request,"recipient_profile.html",{"recipient":recipient})   

def edit_recipient(request,id):
    recipient=Recipient.objects.get(id=id)

    if request.method=="POST":
        form=RecipientRegistrationForm(request.POST,instance=recipient)

        if form.is_valid():
            form.save()
    else:
        form=RecipientRegistrationForm(instance=recipient)
    return render(request,"edit_recipient.html",{"form":form})    

def delete_recipient(request,id):
    recipient=Recipient.objects.get(id=id)
    if request.method == 'POST':
        recipient.delete()
        return redirect(recipient_list)
    return render (request,'delete_recipient.html')