from django.contrib.auth.models import User
from . models import *
# Create your views here.
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import auth
def addbilling(request):
    return render(request,'add-billing.html')
def addprescription(request):
    return render(request,'add-prescription.html')
def appointments(request):
    return render(request,'appointments.html')
def blankpage(request):
    return render(request,'blank-page.html')
def booking(request):
    return render(request,'booking.html')
def bookingsuccess(request):
    return render(request,'booking-success.html')
def calender(request):
    return render(request,'calendar.html')
def changepassword(request):
    return render(request,'change-password.html')
def chat(request):
    return render(request,'chat.html')
def chatdoctor(request):
    return render(request,'chat-doctor.html')
def checkout(request):
    return render(request,'checkout.html')
def components(request):
    return render(request,'components.html')
def doctorchangepassword(request):
    return render(request,'doctor-change-password.html')
def doctordashboard(request):
    return render(request,'doctor-dashboard.html')
def doctorprofile(request):
    return render(request,'doctor-profile.html')
def doctorprofilesettings(request):
    return render(request,'doctor-profile-settings.html')
def doctorregister(request):
    return render(request,'doctor-register.html')
def editbilling(request):
    return render(request,'edit-billing.html')
def editprescription(request):
    return render(request,'edit-prescription.html')
def favorites(request):
    return render(request,'favorites.html')
def forgotpassword(request):
    return render(request,'forgot-password.html')
def index(request):
    results=Location.objects.all
    special = speciality.objects.all
    return render(request, "index.html",{"location":results,"speciality":special})
    # return render(request,'index.html')
def index2(request):
    results = Location.objects.all
    special = speciality.objects.all
    return render(request, "index-2.html", {"location": results, "speciality": special})

def invoiceview(request):
    return render(request,'invoice-view.html')
def invoices(request):
    return render(request,'invoices.html')
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return HttpResponse('Login Successfull!!')
        else:
            return render (request,'login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'login.html')
def mypatients(request):
    return render(request,'my-patients.html')
def patientdashboard(request):
    return render(request,'patient-dashboard.html')
def patientprofile(request):
    return render(request,'patient-profile.html')
def privacypolicy(request):
    return render(request,'privacy-policy.html')
def profilesettings(request):
    return render(request,'profile-settings.html')
# def register(request):
#     return render(request,'register.html')
def register(request):
    if request.method == "POST":
        try:
            User.objects.get(username = request.POST['username'])
            return render (request,'register.html', {'error':'Username is already taken!'})
        except User.DoesNotExist:
            user = User.objects.create_user(request.POST['username'],password=request.POST['password'],email=request.POST['email'],mobile_number=request.POST['mnumber'])
            user.save()
            auth.login(request,user)
            return HttpResponse('signup completed!!')
    else:
        return render(request,'register.html')
def reviews(request):
    return render(request,'reviews.html')
def scheduletimings(request):
    return render(request,'schedule-timings.html')
def search(request):
    return render(request,'search.html')
def socialmedia(request):
    return render(request,'social-media.html')
def termcondition(request):
    return render(request,'term-condition.html')
def videocall(request):
    return render(request,'video-call.html')
def voicecall(request):
    return render(request,'voice-call.html')
############################################################
