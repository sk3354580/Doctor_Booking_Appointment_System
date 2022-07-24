from django.contrib import admin
from . models import *
# Register your models here.
class blogss(admin.ModelAdmin):
    list_display = ('id','title','description','date')
admin.site.register(Blogs,blogss)