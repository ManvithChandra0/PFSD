from django import forms
from .models import BioData

class BioDataForm(forms.ModelForm):
    class Meta:
        model = BioData
        fields = ['name', 'age', 'address', 'email', 'phone']