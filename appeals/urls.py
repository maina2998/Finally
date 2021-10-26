from django.urls import path
from .views import appeals_list,add_appeals_form

urlpatterns=[
path("list/",appeals_list,name="appeals_list"),
path("appealsform/",add_appeals_form,name="add_appeals_form"),
                       
]