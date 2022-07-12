from statistics import mode
from django.db import models
# Create your models here.

class customer(models.Model):
    customer_name = models.CharField(max_length=100)
    contact = models.IntegerField()
    address = models.CharField(max_length=100)

class menu(models.Model):
    pizza_name = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    is_veg = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.pizza_name}, {self.price}, {self.quantity}, {self.is_veg}'


class order(models.Model):
    customer_id = models.ForeignKey(customer, on_delete=models.CASCADE, related_name='customer_id')
    pizza_id = models.ForeignKey(menu, on_delete=models.CASCADE, related_name='pizza_id')
    quantity = models.IntegerField()
    total_amount = models.IntegerField()
