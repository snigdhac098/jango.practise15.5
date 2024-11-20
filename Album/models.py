from django.db import models
from A_Musician.models import Musicianmodel

class Album_model(models.Model):
    Album_name=models.CharField(max_length=100,null=True,blank=True)
    Album_release_Date=models.DateField(null=True,blank=True)
    Musician=models.ForeignKey(Musicianmodel,on_delete=models.CASCADE,null=True,blank=True)
    NUM_SIZES = {
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5"
    }
    Rating = models.CharField(max_length=5, choices=NUM_SIZES,null=True,blank=True)


    def __str__(self):
        return self.Album_name
