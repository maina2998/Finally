from django.shortcuts import render,redirect

from appeals.forms import Addappealforms
from .models import Appeals

def appeals_list(request):
    appeal=Appeals.objects.all()
    return render(request,"appeals_list.html",{"appeals":appeal})

def add_appeals_form(request):
    if request.method=="POST":
        form=add_appeals_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_appeals_form")
        else:
            print(form.errors)
    else:
        form=Addappealforms()

    return render(request,"add_appeals_form.html",{"form":form})


