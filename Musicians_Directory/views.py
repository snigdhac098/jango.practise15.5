from django.shortcuts import render
from Album.models import Album_model

def home(request):
    data=Album_model.objects.all()
    return render(request,'homepage.html',{'data' : data})