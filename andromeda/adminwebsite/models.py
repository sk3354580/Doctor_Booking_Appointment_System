from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
class doctor_profile(models.Model):
    ############basic information
    image = models.ImageField(upload_to='uploads/')
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
    clinic_images = models.ImageField()
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




