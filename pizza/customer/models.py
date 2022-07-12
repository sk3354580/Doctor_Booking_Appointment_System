from django.db import models
class customer(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    address = models.CharField(max_length=30)
class menu(models.Model):
    pname = models.CharField(max_length=10)
    is_veg = models.BooleanField(default=True)
    quantity = models.IntegerField()
    price = models.IntegerField()

class order(models.Model):
    
    customer_id = models.ForeignKey(customer, on_delete=models.CASCADE, related_name='customer_id')
    pizza_id = models.ForeignKey(menu, on_delete=models.CASCADE, related_name='pizza_id')
    quantity = models.IntegerField()
    total_amount = models.IntegerField()
