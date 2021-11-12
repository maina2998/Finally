from django.shortcuts import render
from .models import Donor
from django.shortcuts import redirect, render
from .forms import donorRegistrationForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register_donor(request):
    if request.method=="POST":
      form=donorRegistrationForm(request.POST,request.FILES)
      if form.is_valid():
            form.save()
      else:
            print(form.errors)
    else:
        form=donorRegistrationForm()
    return render(request,"register_donor.html",{"form":form})
def donor_list(request):
    donors=Donor.objects.all()
    return render(request,"donor_list.html",{"donors":donors})

def edit_donor(request,id):
    donors=Donor.objects.get(id=id)
    if request.method=="POST":
        form=donorRegistrationForm(request.POST,instance=donors)
        if form.is_valid():
            form.save()
    else:
        form=donorRegistrationForm(instance=donors)
    return render(request,"edit_donor.html",{"form":form})

def donor_profile(request,id):
    donors=Donor.objects.get(id=id)
    return render(request,"donor_profile.html",{"donor":donors})

def delete_donor(request,id):
    donor=Donor.objects.get(id=id)
    if request.method == 'POST':
        donor.delete()
        return redirect(donor_list)
    return render (request,'delete_donor.html')




