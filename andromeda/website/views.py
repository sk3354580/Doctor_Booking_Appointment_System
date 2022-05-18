
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse


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
    if request.method == 'POST':
        from_time = request.POST['ftime']
        to_time = request.POST['totime']
        date = request.POST['date']
        first_name = request.POST['cfname']
        last_name = request.POST['clname']
        email = request.POST['cemail']
        phoneNumber = request.POST['cmnumber']
        Payment_card = request.POST['nameoncard']
        card_number = request.POST['cardnumber']
        expire_month = request.POST['expirymonth']
        expire_year = request.POST['expiryyear']
        Cvv = request.POST['cvv']
        card = appointment_booking(
            from_time = from_time,
            to_time = to_time,
            date = date,
            first_name = first_name,
            last_name = last_name,
            email = email,
            phoneNumber = phoneNumber,
            Payment_card = Payment_card,
            card_number = card_number,
            expire_month = expire_month,
            expire_year = expire_year,
            Cvv = Cvv)
        card.save()
        return HttpResponse("your transactions is proceessing !!!!!!!!!")
    else:
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
    if request.method == 'POST':
        image = request.POST['image']
        username = request.POST['username']
        email = request.POST['email']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        phone_number = request.POST['mnumber']
        date_of_birth = request.POST['dob']
        biography = request.POST['biography']
        clinic_name = request.POST['clinicname']
        clinic_address = request.POST['clinicadress']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        postalcode = request.POST['postalcode']
        services = request.POST['services']
        specialist = request.POST['specialist']
        degree = request.POST['degree']
        college = request.POST['college']
        yoc = request.POST['yoc']
        hospitalname = request.POST['hospitalname']
        froms = request.POST['froms']
        to = request.POST['to']
        designation = request.POST['designation']
        awards = request.POST['awards']
        year = request.POST['year']
        memberships = request.POST['memberships']
        registrations = request.POST['registrations']
        registrationyear = request.POST['registrationyear']
        clinic_image = request.POST['clinicimage']
        b = doctor_profile(username=username,
                               first_name=firstname,
                               last_name=lastname,
                               Biography=biography,
                               clinic_name=clinic_name,
                               clinic_address=clinic_address,
                               Address_line1=address1,
                               Address_line2=address2,
                               City=city,
                               State_Provice=state,
                               Country=country,
                               Services=services,
                               Specialiazation=specialist,
                               Degree=degree,
                               College_Institute=college,
                               Hospital_Name=hospitalname,
                               Designation=designation,
                               Awards=awards,
                               Memberships=memberships,
                               Registrations=registrations,
                               Date_of_Birth=date_of_birth,
                               Year_of_Completion=yoc,
                               From=froms,
                               To=to,
                               Year=year,
                               Year_of_Registeration=registrationyear,
                               email=email,
                               image=image,
                               clinic_images=clinic_image,
                               Postal_code=postalcode,
                               phoneNumber=phone_number)
        b.save()
        return redirect(all_doctors)
    else:
        return render(request, 'doctor-profile-settings.html')

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
def patientprofilesettings(request): 
    if request.method == 'POST':
        image = request.POST['pimage']
        first_name = request.POST['pfname']
        last_name = request.POST['plname']
        phoneNumber = request.POST['pmnumber']
        Date_of_Birth = request.POST['pdob']
        # Blood_Group = request.POST['']
        email = request.POST['pemail']
        Address =request.POST['paddress']
        City =request.POST['pcity']
        State =request.POST['pstate']
        zip_code =request.POST['pzipcode']
        Country =request.POST['pcountry']
        z = patient_profile(
            image = image,
            first_name = first_name,
            last_name = last_name,
            phoneNumber = phoneNumber,
            Date_of_Birth = Date_of_Birth,
            email = email,
            Address = Address,
            City = City,
            State = State,
            zip_code = zip_code,
            Country = Country
        )
        z.save()
        return HttpResponse("saved Successfully !!")
    else:
        return render(request,'profile-settings.html')
def privacypolicy(request):
    return render(request,'privacy-policy.html')
def patientprofile(request):
    return render(request,'patient-profile.html')
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

########################################################

def all_doctors(request):
    pizzas = doctor_profile.objects.all()
    return render(request, 'all_doctors.html', {'pizzas': pizzas})


def doctor_info(request, ids):
    a = doctor_profile.objects.get(id=ids)
    return render(request, "doctor-profile.html", {'detail': a})


def doctor_edit(request, id):
    pizza_retrieved = doctor_profile.objects.get(id=id)
    if request.method == "POST":
        # pizza_retrieved.name = request
        pizza_name = request.POST['name']
        pizza_size = request.POST['size']
        pizza_price = request.POST['price']

        pizza_retrieved.name = pizza_name
        pizza_retrieved.price = pizza_price
        pizza_retrieved.size = pizza_size
        pizza_retrieved.save()

        return HttpResponseRedirect(reverse('pizza'))
    else:
        return render(request, "hello/pizza_edit.html", {'pizza': pizza_retrieved})


def doctor_delete(request, id):
    a = doctor_profile.objects.get(id=id)
    a.delete()
    return HttpResponseRedirect(reverse('all_doctors'))
###################POpular section