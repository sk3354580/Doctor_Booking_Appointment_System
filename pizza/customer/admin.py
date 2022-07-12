from django.contrib import admin
from . models import customer, menu,order
# Register your models here.
class client(admin.ModelAdmin):
    list_display = ('name','phone','address')
admin.site.register(customer,client)

class menus(admin.ModelAdmin):
    list_display = ('pname','is_veg','quantity','price')
admin.site.register(menu,menus)

class orders(admin.ModelAdmin):
    list_display = ('customer_id','pizza_id','quantity','total_amount')
admin.site.register(order,orders)