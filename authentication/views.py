
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import  Users
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import Users,auth

def home(request):
    return render(request, "authentication\home.html")

def signup(request):
    if request.method =='POST':
        f_name=request.POST['firstName']        
        l_name=request.POST['lastName']
        Email=request.POST['email']
        mobile=request.POST['mobile']
        password  =request.POST['password']
        c_password  =request.POST['cpassword'] 
        my_model=Users.objects.create_user(first_name=f_name,last_name=l_name, email =Email, mobile =mobile,password=password)
        my_model.save()
        print('user created')
        return  redirect(request,"authentication/signin.html")
    else:
        return render(request, "authentication/signup.html")
 


def signin(request):
    return render(request, "authentication/signin.html")

def user_logout(request):
    #logout(request)
    messages.success(request, "Logout successful.")
    return redirect('signin')

def forgetpass(request):
    return render(request, "authentication/forgetpass.html")

def employee(request):
    return render(request, "authentication/employee.html")

def student(request):
    return render(request, "authentication/student.html")

def admino(request):
    return render(request, "authentication/admino.html")

def attendance_entry(request):
    return render(request, "authentication/attendance_entry.html")

def sms_alert(request):
    return render(request, "authentication/sms_alert.html")

def updation(request):
    return render(request, "authentication/updation.html")

def timeadjustment(request):
    return render(request, "authentication/timeadjustment.html")

def update(request):
    return render(request, "authentication/update.html")

def student_leave(request):
    return render(request, "authentication/student-leave.html")