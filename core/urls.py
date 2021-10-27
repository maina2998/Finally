from django.urls import path
from .views import login_user,log_out_user

urlpatterns=[
    path('', login_user, name="login"),
]