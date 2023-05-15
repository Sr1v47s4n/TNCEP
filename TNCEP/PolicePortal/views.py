from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Police
# Create your views here.
def index(request):
    return render(request, "Police/index.html")

def signup_usr(request):
    if request.method == "POST":
        police_name = request.POST["police_name"]
        police_email = request.POST["police_email"]
        police_phno = request.POST["police_phno"]
        police_city = request.POST["police_city"]
        police_locality = request.POST["police_locality"]
        police_post = request.POST["police_post"]
        password1 = request.POST.get["password1"]
        password2 = request.POST.get["password2"]
        if password1 == password2:
            police = Police(police_name=police_name,police_phno=police_phno,police_city=police_city,police_email=police_email,police_locality=police_locality,police_post=police_post,password=password1)
            police.save()
            return redirect("login",{"message":"Successfuly Signed Up"})
        else:
            return render(request, "Police/signup.html",{"message":"Something Went Wrong"})
        
        
def login_usr(request):
    try:
        if request.method == "POST":
            smem = request.method.POST.get["smem"]
            username = request.POST["username"]
            password = request.POST.get["password"]
            if smem == "Email":
                user = authenticate(request,police_email=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect("home")
                else:
                    return render(request,"login.html",{"message":"Invalid User"})
            else:
                user = authenticate(request,police_phno=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect("home")
                else:
                    return render(request,"login.html",{"message":"Invalid User"})                    
    except Police.DoesNotExist:
        return render(request,"Police/login.html",{"meassage":"User Not exist"})    
                    
@login_required(login_url="police_login")
def logout(request):
    logout(request)
    return redirect("Polic/login")

