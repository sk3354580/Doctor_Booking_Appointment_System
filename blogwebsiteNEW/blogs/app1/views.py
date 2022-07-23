
from django.shortcuts import render,HttpResponse,redirect

from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.core.mail import send_mail
import uuid
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from . EmailBackend import EmailBackEnd
from .models import *
from django.contrib.auth.decorators import login_required
def register_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            if User.objects.filter(username=username).first():
                messages.warning(request, 'username already exists')
                return redirect('/register')

            elif User.objects.filter(email=email).first():
                messages.warning(request, 'email already exists')
                return redirect('/register')

            user_obj = User.objects.create(username=username, email=email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user=user_obj, auth_token=auth_token)
            profile_obj.save()

            send_mail_after_registration(email, auth_token)

            return redirect('/token')
        except Exception as e:
            print(e)

    return render(request, 'register.html')


def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_obj = User.objects.filter(email=email).first()

        if user_obj is None:
            messages.warning(request, 'user not found')
            return redirect('/login')
        profile_obj = Profile.objects.filter(user=user_obj).first()

        if not profile_obj.is_verified:
            messages.warning(request, 'Your account is not verified yet.check your mail')
            return redirect('/login')
        user = EmailBackEnd.authenticate(request, username=email, password=password)
        if user is None:
            messages.warning(request, 'invalid email or password')
            return redirect('/login')
        login(request, user)
        return redirect('/')

    return render(request, 'login.html')


def verify(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token=auth_token).first()
        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'your profile is already verified')
                return redirect('/login')

            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Congratulation Your Email Has Verified successfully')
            return redirect('/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)


def error_page(request):
    return render(request, 'error.html')


def success(request):
    return render(request, 'success.html')


def token_send(request):
    return render(request, 'token_send.html')


def send_mail_after_registration(email, token):
    subject = "Your Account Needs To Be verified"
    message = f"hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}/"
    email_from = settings.EMAIL_HOST_USER
    receipt_list = [email]
    send_mail(subject, message, email_from, receipt_list)



# Create your views here.
def blogindex(request):
    allblogs = Blogs.objects.all()
    return render(request,'blogindex.html',{'allblogs':allblogs})

def editprofile(request):
    return render(request,'editprofile.html')

@login_required(login_url='/login')
def commentonblog(request,id):

    blogname = Blogs.objects.filter(id=id)
    if request.method == 'POST':
        comments = request.POST['comment']
        commentsave = comment(
            blogname = blogname,
            commentatorname = request.user,
            commentonblog = comments,
        )
        commentsave.save()
        return HttpResponse("comments is done")
    else:
        return render(request,'comments.html',{'id':id})

@login_required(login_url='/login')
def createblog(request):
    ids = request.user
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        blog = Blogs(
            blodid = ids,
            title = title,
            description = description
        )
        blog.save()
        return redirect('blogindex')
    else:
        return render(request,'createblog.html')

@login_required(login_url='/login')
def blogdelete(request,id):
    blog_delete = Blogs.objects.get(id=id)
    blog_delete.delete()
    return redirect('blogindex')
def totalviews(request):

    return HttpResponse('total number of blogs')
def readblog(request,id):
    blogread = Blogs.objects.get(id=id)
    return render(request,'readblog.html',{'blogread':blogread,'id':id})
def bloglogout(request):
    logout(request)
    return redirect('blogindex')

@login_required(login_url='/login')
def blogupdate(request,id):
    updateblog = Blogs.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST['title']
        print(title)
        description = request.POST['description']
        print(description)
        updateblog.title = title
        updateblog.description = description
        updateblog.save()
        return redirect('blogindex')
    else:
        return render(request,'blogupdate.html',{'id':id,'updateblog':updateblog})


