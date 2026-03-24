from django import forms
from .models import Moto

class MotoForm(forms.ModelForm):
    class Meta:
        model = Moto
        fields = ['brand', 'model', 'year', 'license_plate', 'owner_name', 'service_description', 'price']
