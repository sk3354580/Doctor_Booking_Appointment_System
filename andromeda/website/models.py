from django.db import models


class Location(models.Model):
	name = models.CharField(max_length=20)
class speciality(models.Model):
	speciality = models.CharField(max_length=50)

###############################################
