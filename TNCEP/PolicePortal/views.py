from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from .models import Police
from Utility.models import AnonComplaint, EmergencyComplaint, NormalComplaint
# Create your views here.

def home(request):
    return render(request, "Police/home.html")


def signup_usr(request):
    if request.method == "POST":
        police_id = generate_user_code()
        police_name = request.POST["police_name"]
        police_email = request.POST["police_email"]
        police_phno = request.POST["police_phno"]
        police_city = request.POST["police_city"]
        police_locality = request.POST["police_locality"]
        police_post = request.POST["police_post"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            police = Police(police_id=police_id,police_name=police_name,police_phno=police_phno,police_city=police_city,police_email=police_email,police_locality=police_locality,police_post=police_post,password=make_password(password1))
            police.save()
            return redirect("Police/login",{"message":"Successfuly Signed Up"})
        else:
            return render(request, "Police/signup.html",{"message":"Something Went Wrong"})
    return render(request, "Police/signup.html")   
        
def login_usr(request):
    if request.method == 'POST':
        police_email = request.POST['police_email']
        password = request.POST['password']

        user = authenticate(request, police_email=police_email, password=password)

        if user is not None:
            login(request, user)
            return redirect('Police/home')
        else:
            return render(request, 'Police/login.html', {'message': 'Invalid User'})

    return render(request, 'Police/login.html')
        
    #     if request.method == "POST":
    #         username = request.POST["username"]
    #         password = request.POST["password"]
    #         print(username,password)
    #         user = authenticate(request,username =username,password=password)
    #         if user is not None:
    #             login(request,user)
    #             return redirect("home")
    #         else:
    #             return render(request,"Police/login.html",{"message":"Invalid User"})
    #     return render(request,"Police/login.html")
    # except Police.DoesNotExist:
    #     return render(request,"Police/login.html",{"meassage":"User Not exist"})    
                    
@login_required(login_url="Police/login")
def logout(request):
    logout(request)
    return redirect("Police/login")

@login_required(login_url="Police/login")
def view_complaints(request):
    complatins = NormalComplaint.objects.filter(complaint_loc=request.user.police_locality, complaint_status="Pending")
    return render(request, "Police/view_complaints.html",{ "complaints":complatins})

@login_required(login_url="Police/login")
def complaintdetails(request,complaint_id):
    details = NormalComplaint.objects.get(complaint_id=complaint_id)
    return render(request, "Police/complaintdetails.html",{"details":details})

@login_required(login_url="Police/login")
def update_status(request,complaint_id):
    if request.method == "POST":
        status = request.POST["status"]
        complaint = NormalComplaint.objects.get(complaint_id=complaint_id)
        complaint.status = status
        complaint.save()
        return redirect("complaints")
    else:
        return redirect("complaints")
    
@login_required(login_url="Police/login")
def solved_complaints(request):
    complaints = NormalComplaint.objects.filter(complaint_status="Solved")
    return render(request, "Police/solved_complaints.html",{"complaints":complaints})



import random
import string

def generate_user_code(length=8):
    characters = string.ascii_letters + string.digits
    user_code = ''.join(random.choice(characters) for _ in range(length))
    return user_code