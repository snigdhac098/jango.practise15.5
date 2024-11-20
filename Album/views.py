from django.shortcuts import render,redirect
from .forms  import Album_form
from . import models
from A_Musician import forms

# Create your views here.

def album(request):
   if request.method == "POST":
         album_form=Album_form(request.POST)
         if album_form.is_valid():
              album_form.save()
              return redirect('album')
   else:
          album_form=Album_form()
   return render (request,'home.html',{'form': album_form})





def edit_musician(request,id):
     post=models.Musicianmodel.objects.get(pk=id)
     post_form=forms.MusicianForm(instance=post)
     if request.method == "POST":
         post_form=forms.MusicianForm(request.POST,instance=post)
         if post_form.is_valid():
              post_form.save()
              return redirect('musican')
   #   else:
   #      post_form=forms.PostForm()
     return render (request,'index.html',{'form':post_form })


def edit_album(request,id):
     post=models.Album_model.objects.get(pk=id)
     post_form=Album_form(instance=post)
     if request.method == "POST":
         post_form=forms.Album_form(request.POST,instance=post)
         if post_form.is_valid():
              post_form.save()
              return redirect('album')
   #   else:
   #      post_form=forms.PostForm()
     return render (request,'home.html',{'form':post_form })




def delete_table(request,id):
     print("hi ......")
     post=models.Album_model.objects.get(pk=id)
     post.delete()
     return redirect('album')
  
  