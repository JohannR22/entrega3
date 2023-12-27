from django import forms
from .models import empleados

class empleadosForm(forms.ModelForm):
    class Meta:
        model = empleados
        fields = '__all__'