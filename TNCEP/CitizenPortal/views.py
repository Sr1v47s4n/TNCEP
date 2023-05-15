from django.shortcuts import render, redirect
from .models import Citizen
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "index.html")

def signup_usr(request):
    try:
        if request.method == "POST":
            citizen_fname = request.POST["citizen_fname"]
            citizen_email = request.POST["citizen_email"]
            citizen_phno = request.POST["citizen_phno"]
            citizen_city = request.POST["citizen_city"]
            citizen_locality = request.POST["citizen_locality"]
            citizen_dob = request.POST["citizen_dob"]
            citizen_address = request.POST["citizen_address"]
            citizen_pincode = request.POST["citizen_pincode"]
            citizen_password = request.POST["citizen_password"]
            citizen_confirm_password = request.POST["citizen_confirm_password"]
            if citizen_password == citizen_confirm_password:
                citizen = Citizen(citizen_fname=citizen_fname, citizen_email=citizen_email, citizen_phno=citizen_phno, citzen_state=citzen_state, citizen_city=citizen_city, citizen_locality=citizen_locality, citizen_dob=citizen_dob, citizen_address=citizen_address, citizen_pincode=citizen_pincode, password=citizen_password)
                citizen.save()
                return redirect("login")
            else:
                return redirect("signup")
        else:
            return render(request, "signup.html")
        
    except:
        return redirect("signup", {"error": "Something went wrong!"})
    
def login_usr(request):
    try:
        if  request.method == "POST":
            em_ph = request.POST["smem"]
            username = request.POST["username"]
            if em_ph == "Email":
                citizen_password = request.POST["password"]
                citizen = authenticate(request, citizen_email=username, password=citizen_password)
                if citizen is not None:
                    login(request, citizen)
                    return redirect("index")
                else:
                    return render(request,"login.html", {"error": "Invalid credentials!"})
            else:
                citizen_password = request.POST["password"]
                citizen = authenticate(request, citizen_phno=username, password=citizen_password)
                if citizen is not None:
                    login(request, citizen)
                    return redirect("index")
                else:
                    return redirect("login", {"error": "Invalid credentials!"})
        return render(request,"login.html")
    except Citizen.DoesNotExist:
        return redirect("login", {"error": "User Does Not Exist!"})

@login_required(login_url="login")
def logout(request):
    logout(request)
    return redirect("login",{ "message": "Logged out successfully!"})
