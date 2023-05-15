from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_usr, name="login_usr"),
    path("signup/", views.signup_usr,name="signup_usr" ),
    path("logout/",views.logout, name="logout"),
]
    