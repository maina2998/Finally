from django.shortcuts import render,redirect

from appeals.forms import Addappealforms
from .models import Appeals

def appeals_list(request):
    appeal=Appeals.objects.all()
    return render(request,"appeals_list.html",{"appeals":appeal})


def add_appeals_form(request):
    if request.method=="POST":
        form=Addappealforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_appeals_form")
        else:
            print(form.errors)
    else:
        form=Addappealforms()

    return render(request,"add_appeals_form.html",{"form":form})

def appeals_profile(request,id):
    appeal=Appeals.objects.get(id=id)
    return render(request,"appeals_profile.html",{"appeal":appeal})

def edit_appeals(request,id):
    appeal=Appeals.objects.get(id=id)
    if request.method=="POST":
        form=Addappealforms(request.POST,instance=appeal)
        if form.is_valid():
            form.save()
        return redirect("appeals_profile",id=appeal.id)

    else:
        form=Addappealforms(instance=appeal)
        return render (request,"edit_appeals.html",{"form":form})

def delete_appeals(request,id):
    appeal=Appeals.objects.get(id=id)
    appeal.delete()
    return redirect(appeals_list)  

