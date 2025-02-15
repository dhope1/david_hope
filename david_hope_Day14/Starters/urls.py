from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    #path("<str:name>", views.greet_user, name="greet"),
    path("display/", views.display, name="display_home"),
    path("random/", views.randomHTML, name="random"), 
    path("<str:name>", views.greet_user_adjusted, name="greet_adjusted")
    ]