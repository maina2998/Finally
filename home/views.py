from django.contrib.auth import logout
from django.shortcuts import redirect, render
from .forms import UserForm #import UserForm and ProfileForm
def user_profile(request):
    user_form = UserForm(instance=request.user)
    return render(request=request, template_name="adminprofile.html", context={"user":request.user, "user_form":user_form, "user_form":user_form })
def userpage(request):
    user_form = UserForm(instance=request.user)
    return render(request=request, template_name="adminprofile.html", context={"user":request.user, "user_form":user_form})
def log_out(request):    
    logout(request)  
    return redirect('login')
def home(request):
    return render(request,"homepage.html")
def login_view(request):
    form = Login(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")    
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'
    return render(request, "accounts/login.html", {"form": form, "msg": msg})






