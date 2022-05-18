from django.contrib import admin
from . models import *
# Register your models here.
class userDB(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Location,userDB)
class special(admin.ModelAdmin):
    list_display = ['speciality']
admin.site.register(speciality,special)
class doctor(admin.ModelAdmin):
    list_display = ('id','image','username','email', 'first_name','last_name', 'phoneNumber','Gender','Date_of_Birth',
                        'Biography', 'clinic_name', 'clinic_address', 'clinic_images','Address_line1','Address_line2', 'City',
                        'State_Provice', 'Country','Postal_code',
                        'Pricing',
                        'Services',
                        'Specialiazation',
                        'Degree',
                        'College_Institute',
                        'Year_of_Completion',
                        'Hospital_Name',
                        'From',
                        'To',
                        'Designation',
                        'Awards',
                        'Year',
                        'Memberships',
                        'Registrations',
                        'Year_of_Registeration')
admin.site.register(doctor_profile,doctor)
class patient(admin.ModelAdmin):
    list_display = ('id',
                    'image',
                    'first_name',
                    'last_name',
                    'Date_of_Birth',
                    'Blood_Group',
                    'email',
                    'phoneNumber',
                    'Address',
                    'City',
                    'State',
                    'zip_code',
                    'Country',)
admin.site.register(patient_profile,patient)
class booking(admin.ModelAdmin):
    list_display = ('id',
                    'from_time',
                    'to_time',
                    'date',
                    'first_name',
                    'last_name',
                    'email',
                    'phoneNumber',
                    'Payment_card',
                    'card_number',
                    'expire_month',
                    'expire_year',
                    'Cvv',
                    'amount_paid')
admin.site.register(appointment_booking,booking)