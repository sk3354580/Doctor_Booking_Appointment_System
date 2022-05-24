from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

class user(AbstractUser):
    pass


################search location suggestions
class Location(models.Model):
    name = models.CharField(max_length=20)
class speciality(models.Model):
    speciality = models.CharField(max_length=50)

###############################################

class doctor_profile(models.Model):
    ############basic information
    doctorId = models.OneToOneField(user, on_delete=models.CASCADE, default='', related_name='doctorId')
    doctor_images = models.ImageField(upload_to='images/')
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phoneNumber = PhoneNumberField(unique = True, blank = False)
    Gender = models.BooleanField(default=True)
    Date_of_Birth = models.DateField(max_length=20)
    Biography = models.CharField(max_length=500)
    ####clinic info###################
    clinic_name = models.CharField(max_length=40)
    clinic_address = models.CharField(max_length=100)
    clinic_images = models.ImageField(upload_to='images/')
    ###############contact details
    Address_line1 = models.CharField(max_length=200)
    Address_line2 = models.CharField(max_length=100)
    City = models.CharField(max_length=30)
    State_Provice = models.CharField(max_length=30)
    Country = models.CharField(max_length=30)
    Postal_code = models.IntegerField()
    ###########pricing ############
    Pricing = models.BooleanField(default=True)
    # Services_and_Specialization##################
    Services = models.CharField(max_length=30)
    Specialiazation = models.CharField(max_length=30)
    ###########Education ###################
    Degree = models.CharField(max_length=30)
    College_Institute = models.CharField(max_length=100)
    Year_of_Completion = models.DateField(max_length=20)
    ##############Experience ######################
    Hospital_Name = models.CharField(max_length=50)
    From = models.DateField(max_length=20)
    To = models.DateField(max_length=20)
    Designation = models.CharField(max_length=50)
    ############awards ######################
    Awards = models.CharField(max_length=30)
    Year = models.DateField(max_length=20)
    #############memberships ######################3
    Memberships = models.CharField(max_length=50)
    #################Registerations #################
    Registrations = models.CharField(max_length=50)
    Year_of_Registeration = models.DateField(max_length=20)



    ####this is patient profile######################
class patient_profile(models.Model):
    patientId = models.OneToOneField(user, on_delete=models.CASCADE, default='', related_name='patientId')
    patient_images = models.ImageField(upload_to='images/')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    Date_of_Birth = models.DateField(max_length=20)
    Blood_Group = models.CharField(max_length=5)
    email = models.EmailField(max_length=50)
    phoneNumber = PhoneNumberField(unique=True, blank=False)
    Address = models.CharField(max_length=200)
    City = models.CharField(max_length=30)
    State = models.CharField(max_length=30)
    zip_code = models.IntegerField()
    Country = models.CharField(max_length=30)
########## this is booking section##################
class appointment_booking(models.Model):
    doctor_id = models.ForeignKey(doctor_profile, on_delete = models.CASCADE, related_name = "doctor_id")
    patient_id = models.ForeignKey(patient_profile, on_delete = models.CASCADE, related_name = "patient_id")
    from_time = models.TimeField(max_length=20)
    to_time = models.TimeField(max_length=20)
    date = models.DateField(max_length=10)
    ##########Payment Method #########################
    Payment_card = models.CharField(max_length=50) ##credit or debit
    card_number = models.IntegerField()
    expire_month = models.IntegerField()
    expire_year = models.IntegerField()
    Cvv = models.IntegerField()
    amount_paid = models.IntegerField()
