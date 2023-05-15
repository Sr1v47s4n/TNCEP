from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_usr, name="login_usr"),
    path("signup/", views.signup_usr,name="signup_usr" ),
    path("logout/",views.logout, name="logout"),
    path("complaints/", views.view_complaints , name="complaints"),
    path("complaint/status", views.status , name="citizen-complaint-status"),
    path("complaint/delete/", views.delete_complaint, name="citizen-complaint-delete"),
    path("emergency_complaint/", views.emergency_complaint, name="emergency-complaint"),
    path("anon_complaint/", views.anon_complaint, name="anon-complaint"),
    path("complaint/", views.normal_complaint , name="complaint"),
    path("about/", views.about , name="about"),
    path("home/", views.home , name="home"),
]
    