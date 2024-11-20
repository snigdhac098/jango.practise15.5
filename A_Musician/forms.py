from django import forms
from . models import Musicianmodel


class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musicianmodel
        fields = '__all__'