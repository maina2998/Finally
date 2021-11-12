from django.urls import path
from .views import edit_recipient,register_recipient,recipient_list,recipient_profile,delete_recipient

from django.conf import settings


urlpatterns=[
    path("register/",register_recipient,name="register_recipient"),
    path("list/",recipient_list,name="recipient_list"),   
    path("edit/<int:id>/",edit_recipient,name="edit_recipient"),
    path("profile/<int:id>/",recipient_profile,name="recipient_profile"),
    path("delete/<int:id>/",delete_recipient,name="delete_recipient"),

]