from django.contrib import admin
from . models import *
# Register your models here.
class userDB(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Location,userDB)
class special(admin.ModelAdmin):
    list_display = ['speciality']
admin.site.register(speciality,special)