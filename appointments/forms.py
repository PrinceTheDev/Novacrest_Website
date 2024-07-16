from django import forms
from .models import Appointments

class AppointmentForm(forms.ModelForm):
    class meta:
        model = Appointments
        fields = ['name', 'email', 'phone', 'date', 'time', 'message']
