from django.db import models

# Create your models here.

class todotitle(models.Model):

    title = models.CharField(max_length=100, unique=True)

class todolist(models.Model):

    title = models.CharField(max_length=100)

    description = models.TextField(null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)

    todo_list = models.ForeignKey(todotitle, on_delete=models.CASCADE)
