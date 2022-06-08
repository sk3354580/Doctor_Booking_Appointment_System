from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
class CustomUser(AbstractUser):
    user_type_data=((1,"Admin"),(2,"Doctor"),(3,"Patient"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)
###############ADMIN ###############
class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    Admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

################## doctor
class Doctor(models.Model):
    id=models.AutoField(primary_key=True)
    doctor=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

######################## patients
class Patient(models.Model):
    id=models.AutoField(primary_key=True)
    patient=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

#
# @receiver(post_save,sender=CustomUser)
# def create_user_profile(sender,instance,created,**kwargs):
#     if created:
#         if instance.user_type==1:
#             Admin.objects.create(Admin=instance)
#         if instance.user_type==2:
#             Doctor.objects.create(Doctor=instance)
#         if instance.user_type==3:
#             Patient.objects.create(Patient=instance)
#
# @receiver(post_save,sender=CustomUser)
# def save_user_profile(sender,instance,**kwargs):
#     if instance.user_type==1:
#         instance.Admin.save()
#     if instance.user_type==2:
#         instance.Doctor.save()
#     if instance.user_type==3:
#         instance.Patient.save()
