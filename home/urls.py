from django.urls import path   

from .views import home
from home import views

app_name ='home'
urlpatterns=[
    path("home/", home ,name="homepage.html"),
    path("user", views.userpage, name = "userpage")    


]
    