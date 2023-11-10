from django.shortcuts import render,redirect 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    return render(request,'index.html') 

def login(request):
    if request.method=="POST":
        username= request.POST['username']
        password= request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None :
            auth_login(request, user) 
            return render(request,'dash.html')
        else:
            return HttpResponse('ERROR!!!!!')
    return render(request,'login.html')


def sign_up(request):
    if request.method=="POST":
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email=request.POST['email']
        if password1==password2:
            if CustomUser.objects.filter(username=username).exists():
                return HttpResponse("User name is already taken")
            else :
                user=CustomUser.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                auth_login(request,user)
                return redirect ('dashboard')
        else:
            return HttpResponse("Pasword does not match")    



    return render(request,'signup.html')

@login_required
def dashboard(request):
    return render(request,'dash.html')



def logout_view(request):
    logout (request)
    return redirect ("login")
