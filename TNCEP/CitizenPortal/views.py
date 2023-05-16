from django.shortcuts import render, redirect
from .models import Citizen
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Utility.models import NormalComplaint, EmergencyComplaint, AnonComplaint
from django.contrib.auth.hashers import make_password


def home(request):
    return render(request, "home.html")

def signup_usr(request):
    try:
        if request.method == "POST":
            citizen_fname = request.POST.get("citizen_fname")
            citizen_email = request.POST.get("citizen_email")
            citizen_phno = request.POST.get("citizen_phno")
            citizen_aadhaar = request.POST.get("citizen_aadhaar")
            citizen_caahaar = request.POST.get("citizen_caahaar")
            citizen_password = request.POST.get("citizen_password")
            citizen_confirm_password = request.POST.get("citizen_confirm_password")
            
            if citizen_aadhaar == citizen_caahaar:
                if citizen_password == citizen_confirm_password:
                    citizen = Citizen(
                        citizen_fname=citizen_fname,
                        citizen_email=citizen_email,
                        citizen_phno=citizen_phno,
                        citizen_aadhaar=citizen_aadhaar,
                        password=make_password(citizen_password)
                    )
                    citizen.save()
                    print("Saved")
                    return redirect("login_usr")
                else:
                    print("Passwords do not match")
                    return render(request, "signup.html", {"message": "Passwords do not match"})
            else:
                print("Aadhaar numbers do not match")
                return render(request, "signup.html", {"message": "Aadhaar numbers do not match"})
    
        return render(request, "signup.html")
    except Exception as e:
        print(e)
        return render(request, "signup.html", {"error": "Something went wrong: " + str(e)})

        # return redirect("signup", {"error": "Something went wrong!"})
    
def login_usr(request):
    try:
        if  request.method == "POST":
            aadhaar = request.POST["aadhaar"]
            citizen_password = request.POST.get("password")
            citizen = authenticate(request, citizen_aadhaar=aadhaar, password=citizen_password)
            if citizen is not None:
                login(request, citizen)
                return redirect("register")
            else:
                return render(request,"login.html", {"message": "Invalid credentials!"})
          
        return render(request,"login.html")
    except Citizen.DoesNotExist:
        return redirect("login_usr", {"message": "User Does Not Exist!"})

@login_required(login_url="login_usr")
def logout_usr(request):
    logout(request)
    return redirect("login_usr",{ "message": "Logged out successfully!"})

@login_required(login_url="login_usr")
def normal_complaint(request):
    if request.method == "POST":
        try:
            complaint_type = request.POST.get("complaint_type")
            complaint_desc = request.POST.get("complaint_desc")
            complaint_loc = request.POST.get("complaint_loc")
            complaint_image = request.FILES.get("complaint_image")
            complaint_video = request.FILES.get("complaint_video")
            complaint_citizen = request.user.citizen_id
            complaint = NormalComplaint(complaint_type=complaint_type, complaint_desc=complaint_desc, complaint_loc=complaint_loc, complaint_image=complaint_image, complaint_video=complaint_video, complaint_citizen=complaint_citizen)
            complaint.save()
            return render(request, "success.html", {"message": "Complaint Registered Successfully","id": complaint.complaint_id})
        except Citizen.DoesNotExist:
            return redirect("login_usr")
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
            
            complaint = EmergencyComplaint(complaint_type=complaint_type, complaint_desc=complaint_desc, complaint_loc=complaint_loc, complaint_image=complaint_image, complaint_video=complaint_video)
            complaint.save()
            return render(request, "success.html", {"message": "Complaint Registered Successfully","id": complaint.complaint_id})
        except Citizen.DoesNotExist:
            return redirect("login_usr")
        except:
            return render(request, "emergency_complaint.html", {"error": "Invalid Details"})
    return render(request,"emergency_complaint.html")

@login_required(login_url="login_usr")
def anon_complaint(request):
    if request.method == "POST":
        try:
            complaint_type = request.POST.get("complaint_type")
            complaint_desc = request.POST.get("complaint_desc")
            complaint_loc = request.POST.get("complaint_loc")
            complaint_image = request.FILES.get("complaint_image")
            complaint_video = request.FILES.get("complaint_video")
            complaint_citizen = request.user.citizen_id
            complaint = AnonComplaint(complaint_type=complaint_type, complaint_desc=complaint_desc, complaint_loc=complaint_loc, complaint_image=complaint_image, complaint_video=complaint_video, complaint_citizen=complaint_citizen)
            complaint.save()
            return render(request, "success.html", {"message": "Complaint Registered Successfully","id": complaint.complaint_id})
        except:
            return render(request, "anon_complaint.html", {"error": "Invalid Details"})
    return render(request,"anon_complaint.html")

@login_required(login_url="login_usr")
def view_complaints(request):
    try:
        complaints = NormalComplaint.objects.filter(complaint_citizen=request.user)
        return render(request, "view_complaints.html", {"complaints": complaints})
    except Citizen.DoesNotExist:
        return redirect("login_usr")

@login_required(login_url="login_usr")
def status(request):
    if request.method == "POST":
        try:
            com_type = request.POST.get("com_type")
            id = request.POST.get("id")
            if  com_type == "Normal":
                complaint = NormalComplaint.objects.get(complaint_id=id)
                return render(request, "status.html", {"complaint": complaint})
            elif com_type == "Anon":
                complaint = AnonComplaint.objects.get(complaint_id=id)
                return render(request, "status.html", {"complaint": complaint})
            else:
                complaint = "Not Found"
                
            return render(request, "status.html", {"complaint": complaint})
        except:
            return render(request, "status.html", {"error": "Invalid Details"})
    return render(request, "status.html")
    
# 6 Hrs only time
@login_required(login_url="login_usr")
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

def register(request):
    return render(request, "register.html")