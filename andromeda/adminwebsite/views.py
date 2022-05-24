from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from website.models import *
# Create your views here.
def admine(request):
    allPatients = patient_profile.objects.all()
    allDoctors = doctor_profile.objects.all()
    countappointment = appointment_booking.objects.all().count()
    countdoctor = doctor_profile.objects.all().count()
    countpatient = patient_profile.objects.all().count()
    context = {'countpatient': countpatient,
               'countdoctor': countdoctor,
               'countappointment':countappointment,
               'allDoctors': allDoctors,
               'allPatients':allPatients}

    return render(request,'admin.html',context)
def appointment_list(request):
    return render(request,'appointment-list.html')
def blank_pagew(request):
    return render(request,'blank-pagew.html')
def componentsw(request):
    return render(request,'componentsw.html')
def data_tables(request):
    return render(request,'data-tables.html')
def doctor_list(request):
    doctorList = doctor_profile.objects.all()
    return render(request,'doctor-list.html', {'doctorList': doctorList})
def error_404(request):
    return render(request,'error-404.html')
def error_500(request):
    return render(request,'error-500.html')
def forgot_passwordw(request):
    return render(request,'forgot-passwordw.html')
def form_basic_inputs(request):
    return render(request,'form-basic-inputs.html')
def form_horizontal(request):
    return render(request,'form-horizontal.html')
def form_input_groups(request):
    return render(request,'form-input-groups.html')
def form_mask(request):
    return render(request,'form-mask.html')
def form_validation(request):
    return render(request,'form-validation.html')
def form_vertical(request):
    return render(request,'form-vertical.html')
def invoice_report(request):
    return render(request,'invoice-report.html')
def invoice(request):
    return render(request,'invoice.html')
def lock_screen(request):
    return render(request,'lock-screen.html')

def loginw(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect(admine)
        else:
            return render (request,'loginw.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'loginw.html')
def patient_list(request):
    patientList = patient_profile.objects.all()
    return render(request,'patient-list.html' ,{'patientList':patientList})
def profilew(request,id):
    ProFileW = doctor_profile.objects.get(id=id)
    return render(request, 'profilew.html', {'ProFileW': ProFileW})
def patientProfileshow(request,id):
    patientProfileshow = patient_profile.objects.get(id=id)
    return render(request, 'patientprofilew.html', {'patientProfileshow': patientProfileshow})
def reviewsw(request):
    return render(request,'reviewsw.html')
def settings(request):
    return render(request,'settings.html')
def specialities(request):
    return render(request,'specialities.html')
def table_basic(request):
    return render(request,'table-basic.html')
def transactions_list(request):
    return render(request,'transactions-list.html')
def registerw(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'registerw.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'],email=request.POST['email'])
                auth.login(request,user)
                return redirect(loginw)
        else:
            return render (request,'registerw.html', {'error':'Password does not match!'})
    else:
        return render(request,'registerw.html')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return HttpResponse('Logout successful!!')

