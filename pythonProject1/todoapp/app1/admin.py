from django.contrib import admin
from . models import *
# Register your models here.
class todot(admin.ModelAdmin):
    list_display = ('id','title')
admin.site.register(todotitle,todot)

class todol(admin.ModelAdmin):
    list_display = ('id','title','description','created_date','todo_list')
admin.site.register(todolist,todol)