from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
from .models import rent_payee
from .models import Rentyourhouse
# Create your views here.
def index(request) :
    return render(request,"index.html")

def register(request) :
    if request.method == 'POST' :
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2 :

            if User.objects.filter(username=username).exists() :
               messages.info(request,'Username Taken')
               return redirect('register')
            elif User.objects.filter(email=email).exists() :
               messages.info(request,'email taken already')
               return redirect('register')
            else :
                user =User.objects.create_user(username=username,email=email,password=password1)
                user.save();
                print('user created')
                return redirect('login') 
        else :
            messages.info(request,'password not matching')
            return redirect('register')
        return('/')  
    else :
           return render(request,"register.html")

  

def login(request) :
     if request.method == 'POST' :
         username = request.POST['username']
         password = request.POST['password']
         user = auth.authenticate(username=username,password=password)
         if user is not None :
             request.session['member_id'] = user.id
             auth.login(request,user)
             return redirect('/')
         else :
             messages.info(request,'invalid credentials')
             return redirect('login')
            
     else :
         return render(request,"login.html")


def logout(request) :
    auth.logout(request)
    request.session['member_id'] = 0
    return redirect('/')
   

@login_required(login_url='login')
def booking(request):
    return render(request,"booking.html")

@login_required(login_url='login')
def rent(request):
    return render(request,"rent.html")

def about(request) :
    return render(request,"about.html")  

def FAQ(request) :
    return render(request,"FAQ.html")

@login_required(login_url='login')
def booking2(request):
    p_email=request.POST(p_email)
    p_name=request.POST(p_name)
    p_country=request.POST(p_country)
    rentpayee=rent_payee(p_email=p_email,p_name=p_name,p_country=p_country)
    rentpayee.save();

@login_required(login_url='login')
def rentyourhouse(request) :
    fullname = request.POST["fullname"]
    From = request.POST["From"]
    To = request.POST["To"]
    adults =request.POST["adults"]
    children =request.POST["children"]
    phonenumber= request.POST["phonenumber"]
    appointment = request.POST["appointment"]
    RENTYOURHOUSE = Rentyourhouse(fullname=fullname,From=From,To=To,adults= adults,children=children,phonenumber=phonenumber,appointment=appointment)
    RENTYOURHOUSE.save();
    return render(request,"booking.html")