from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from mysite_app.models import UserA
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def index(request):
    
    return render(request,"index.html")




def register(request):
    
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        roll_no = request.POST['roll_no']
        branch = request.POST['branch']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            passnotmatch = True
            return render(request, "student_registration.html", {'passnotmatch':passnotmatch})

        user = User.objects.create_user(username=username, email=email, password=password,first_name=first_name, last_name=last_name)
        userA= UserA.objects.create(user=user, roll_no=roll_no,phone=phone,branch=branch)
        userA.save()
        user.save()
        
        alert = True
        return render(request, "user_registration.html", {'alert':alert})
    return render(request, "user_registration.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return HttpResponse("You are not a student!!")
            else:
                return redirect("user_profile")
        else:
            alert = True
            return render(request, "user_login.html", {'alert':alert})
    return render(request, "user_login.html")

def admin_login(request):
    if request.method== "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            if request.user.is_superuser:
                return redirect("/admin_p")
            else:
                return HttpResponse("You are not Admin!!!")
        else:
            alert=True
            return render(request,"admin_login.html", {'alert':alert} )
    return render(request,"admin_login.html")    


# def admin_login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)

#         if user is not None:
#             login(request, user)
#             if request.user.is_superuser:
#                 return redirect("/admin.html")
#             else:
#                 return HttpResponse("You are not an admin.")
#         else:
#             alert = True
#             return render(request, "admin_login.html", {'alert':alert})
#     return render(request, "admin_login.html")


def Logout(request):
    pass



def user_profile(request):
    return render(request, "user_profile.html")


def admin_p(request):
    return render(request, "admin_p.html")