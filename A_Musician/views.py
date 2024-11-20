from django.shortcuts import render,redirect
from . import forms

# Create your views here.




def Musician(request):
   if request.method == "POST":
         display_form=forms.MusicianForm(request.POST)
         if display_form.is_valid():
              display_form.save()
              return redirect('musican')
   else:
          display_form=forms.MusicianForm()
   return render (request,'index.html',{'form':display_form})
