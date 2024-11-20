from django import forms
from . models import Album_model


class Album_form(forms.ModelForm):
    class Meta:
        model = Album_model
        fields = '__all__'