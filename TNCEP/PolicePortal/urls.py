from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_usr, name="login_usr"),
    path("signup/", views.signup_usr,name="signup_usr" ),
    path("logout/",views.logout, name="logout"),
    path("", views.home, name="control-home"),
    path("view_complaints/", views.view_complaints, name="control-view_complaints"),
    path("complaintdetails/<int:complaint_id>/", views.complaintdetails, name="control-complaintdetails"),
    path("update_status/<int:complaint_id>/", views.update_status, name="control-update_status"),
    path("solvedcomplaints/", views.solved_complaints, name="control-solvedcomplaints"),
]