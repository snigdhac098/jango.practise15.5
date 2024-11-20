from django.db import models

# Create your models here.


class Musicianmodel(models.Model):
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    Email=models.EmailField()
    Instrument_Type=models.TextField()
    Phone_number=models.CharField(max_length=12)


    def __str__(self):
        return self.First_name
