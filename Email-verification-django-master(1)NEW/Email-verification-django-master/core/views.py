from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.core.mail import send_mail
import uuid
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Profile

# Create your views here.

def home(request):
    return render (request,'home.html')

def register_page(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        try:
            if User.objects.filter(username=username).first():
                messages.warning(request,'username already exists')
                return redirect('/register')

            elif User.objects.filter(email=email).first():
                messages.warning(request,'email already exists')
                return redirect('/register')
            
            user_obj =User.objects.create(username=username,email=email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user=user_obj,auth_token =auth_token)
            profile_obj.save()

            send_mail_after_registration(email,auth_token)

            return redirect ('/token')
        except Exception as e:
            print(e)

    return render (request,'register.html')

def login_page(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user_obj=User.objects.filter(username =username).first()

        if user_obj is None:
            messages.warning(request,'user not found')
            return redirect('/login')
        profile_obj = Profile.objects.filter(user=user_obj).first()

        if not profile_obj.is_verified:
            messages.warning(request,'Your account is not verified yet.check your mail')
            return redirect('/login')
        user = authenticate(username=username,password=password)
        if user is None:
            messages.warning(request,'invalid username or password')
            return redirect('/login')
        login(request,user)
        return redirect ('/')

    return render(request,'login.html')

def verify(request,auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token=auth_token).first()
        if profile_obj:
            if profile_obj.is_verified:
                 messages.success(request,'your profile is already verified')
                 return redirect('/login')
                

            profile_obj.is_verified=True
            profile_obj.save()
            messages.success(request,'Congratulation Your Email Has Verified successfully')
            return redirect ('/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)

def error_page(request):
    return render (request,'error.html')



def success(request):
    return render (request,'success.html')

def token_send(request):
    return render (request,'token_send.html')

def send_mail_after_registration(email,token):
    subject ="Your Account Needs To Be verified"
    message =f"hi paste the link to verify your account http://127.0.0.1:9000/verify/{token}/"
    email_from = settings.EMAIL_HOST_USER
    receipt_list =[email]
    send_mail(subject,message,email_from,receipt_list)
