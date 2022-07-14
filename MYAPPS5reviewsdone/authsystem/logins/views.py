from django.shortcuts import render,HttpResponseRedirect,reverse,HttpResponse,redirect
from . models import  *

from . EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def sortind(request):
    return render(request,'sortind.html')
def index(request):
    return render(request,'index.html')
def admins(request):
    return  render(request,'admin.html')
def doctors(request):
    return render(request,'doctor.html')
def patients(request):
    return render(request,'patient.html')
def do_admin_signup(request):
    if request.method == 'POST':
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=CustomUser.objects.create_user(username=username,password=password,email=email,user_type=1)
        user.save()
        return HttpResponse('admin singup successffull!!!')
    else:
        return render(request,'admin.html')

def do_doctor_signup(request):
    if request.method == 'POST':
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=CustomUser.objects.create_user(username=username,password=password,email=email,user_type=2)

        user.save()

        return HttpResponse('successful')
    else:
        return render(request,'doctor.html')


def do_patient_signup(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = CustomUser.objects.create_user(username=username, password=password, email=email, user_type=3)
        user.save()
        return  HttpResponse('patient signup successful')
    else:
        return render(request,'patient.html')
def logins(request):
    return render(request,'login.html')
def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponse("thi is admin")
            elif user.user_type=="2":
                return HttpResponse('this is doctor section')
            else:
                return HttpResponse('thi is  patient section')
        else:

            return HttpResponseRedirect("/")


