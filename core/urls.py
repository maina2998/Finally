from django.urls import path
from .views import login_user,log_out_user
from core import views

urlpatterns=[
    path('', login_user, name="login"),
    path('signup_user',views.signup_user, name='signup'),
    path("password_reset", views.password_reset_request, name="password_reset"),
]