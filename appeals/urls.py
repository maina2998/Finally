from django.urls import path
from .views import appeals_list,add_appeals_form, delete_appeals, edit_appeals,appeals_profile

urlpatterns=[
path("list/",appeals_list,name="appeals_list"),
path("appealsform/",add_appeals_form,name="add_appeals_form"),
path("edit/<int:id>/",edit_appeals,name="edit_appeals"),
path("profile/<int:id>/",appeals_profile,name="appeals_profile"),
path('delete<int:id>/',delete_appeals,name="delete_appeals"),  


                       
]