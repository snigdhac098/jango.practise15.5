from django.urls import path,include
from . import views

urlpatterns = [
   
    path('',views.album,name="album"),
    path('edit_musician/<int:id>',views.edit_musician,name='edit_musician'),
    path('edit_album/<int:id>',views.edit_album,name='edit_album'),
    path('delete/<int:id>',views.delete_table,name='delete_table')


]