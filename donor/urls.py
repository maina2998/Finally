from django import urls
from django.urls import path
from .views import register_donor,donor_list,edit_donor,donor_profile,delete_donor, donor_profile

urlpatterns = [
    path("register/", register_donor,name="register_donor"),
    path("list/", donor_list,name="donor_list"),
    path("edit/<int:id>", edit_donor,name="edit_donor"),
    path("profile/<int:id>", donor_profile,name="donor_profile"),
    path("delete/<int:id>", delete_donor,name="delete_donor"),
]