from django.db import models

# Create your models here.
class Blogs(models.Model):
    title=models.CharField(max_length=200,null=True)
    description=models.CharField(max_length=1200,null=True)
    date=models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.id) + ':' + str(self.title) + ':' + str(self.description) + ':' + str(self.date)