from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['owner_name', 'pet_name', 'pet_type', 'service', 'date', 'time']
        widgets = {
            'owner_name': forms.TextInput(attrs={'id': 'ownerName', 'class': 'form-control', 'required': True}),
            'pet_name': forms.TextInput(attrs={'id': 'petName', 'class': 'form-control', 'required': True}),
            'pet_type': forms.Select(attrs={'id': 'petType', 'class': 'form-control', 'required': True}),
            'service': forms.Select(attrs={'id': 'service', 'class': 'form-control', 'required': True}),
            'date': forms.DateInput(attrs={'id': 'date', 'class': 'form-control', 'type': 'date', 'required': True}),
            'time': forms.TimeInput(attrs={'id': 'time', 'class': 'form-control', 'type': 'time', 'required': True}),
        }
