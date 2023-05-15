from django.shortcuts import render, redirect
from .models import Citizen
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Utility.models import NormalComplaint, EmergencyComplaint, AnonComplaint


def index(request):
    return render(request, "index.html")

def home(request):
    return render(request, "home.html")

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

@login_required(login_url="login")
def normal_complaint(request):
    if request.method == "POST":
        try:
            complaint_type = request.POST.get("complaint_type")
            complaint_desc = request.POST.get("complaint_desc")
            complaint_loc = request.POST.get("complaint_loc")
            complaint_image = request.FILES.get("complaint_image")
            complaint_video = request.FILES.get("complaint_video")
            complaint_citizen = request.user
            complaint = NormalComplaint(complaint_type=complaint_type, complaint_desc=complaint_desc, complaint_loc=complaint_loc, complaint_image=complaint_image, complaint_video=complaint_video, complaint_citizen=complaint_citizen)
            complaint.save()
            return render(request, "success.html", {"message": "Complaint Registered Successfully","id": complaint.complaint_id})
        except Citizen.DoesNotExist:
            return redirect("login")
        except:
            return render(request, "normal_complaint.html", {"error": "Invalid Details"})
    return render(request,"normal_complaint.html")

def emergency_complaint(request):
    if request.method == "POST":
        try:
            complaint_type = request.POST.get("complaint_type")
            complaint_desc = request.POST.get("complaint_desc")
            complaint_loc = request.POST.get("complaint_loc")
            complaint_image = request.FILES.get("complaint_image")
            complaint_video = request.FILES.get("complaint_video")
            complaint_citizen = request.user
            
            complaint = EmergencyComplaint(complaint_type=complaint_type, complaint_desc=complaint_desc, complaint_loc=complaint_loc, complaint_image=complaint_image, complaint_video=complaint_video, complaint_citizen=complaint_citizen)
            complaint.save()
            return render(request, "success.html", {"message": "Complaint Registered Successfully","id": complaint.complaint_id})
        except Citizen.DoesNotExist:
            return redirect("login")
        except:
            return render(request, "emergency_complaint.html", {"error": "Invalid Details"})
    return render(request,"emergency_complaint.html")

def anon_complaint(request):
    if request.method == "POST":
        try:
            complaint_type = request.POST.get("complaint_type")
            complaint_desc = request.POST.get("complaint_desc")
            complaint_loc = request.POST.get("complaint_loc")
            complaint_image = request.FILES.get("complaint_image")
            complaint_video = request.FILES.get("complaint_video")
            
            complaint = AnonComplaint(complaint_type=complaint_type, complaint_desc=complaint_desc, complaint_loc=complaint_loc, complaint_image=complaint_image, complaint_video=complaint_video)
            complaint.save()
            return render(request, "success.html", {"message": "Complaint Registered Successfully","id": complaint.complaint_id})
        except:
            return render(request, "anon_complaint.html", {"error": "Invalid Details"})
    return render(request,"anon_complaint.html")

@login_required(login_url="login")
def view_complaints(request):
    try:
        complaints = NormalComplaint.objects.filter(complaint_citizen=request.user)
        return render(request, "view_complaints.html", {"complaints": complaints})
    except Citizen.DoesNotExist:
        return redirect("login")

@login_required(login_url="login")
def status(request):
    if request.method == "POST":
        try:
            com_type = request.POST.get("com_type")
            id = request.POST.get("id")
            if  com_type == "Normal":
                complaint = NormalComplaint.objects.get(complaint_id=id)
                # if complaint is  None:
                #     complaint = "Not Found"
            elif com_type == "Anon":
                complaint = AnonComplaint.objects.get(complaint_id=id)
                # if complaint is  None:
                #     complaint = "Not Found"
            else:
                complaint = "Not Found"
            return render(request, "status.html", {"complaint": complaint})
        except:
            return render(request, "status.html", {"error": "Invalid Details"})
    return render(request, "status.html")
    
# 6 Hrs only time
@login_required(login_url="login")
def delete_complaint(request):
    if request.method == "POST":
        try:
            id = request.POST.get("id")
            complaint = NormalComplaint.objects.filter(complaint_id=id, complaint_citizen=request.user)
            if request.POST.get("delete") == "Delete":
                complaint.delete()
                return render(request, "delete_complaint.html", {"message": "Complaint Deleted Successfully"})
            return render(request, "delete_complaint.html", {"details": complaint})
        except:
            return render(request, "delete_complaint.html", {"error": "Invalid Details"})
    return render(request, "delete_complaint.html")

def about(request):
    return render(request, "about.html")

