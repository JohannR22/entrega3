from django import forms
from .models import directivos

class directivosForm(forms.ModelForm):
    class Meta:
        model = directivos
        fields = '__all__' 