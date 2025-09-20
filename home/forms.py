from django import forms
from .models import Availability

class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['time_slot']
        widgets = {
            'time_slot': forms.Select(attrs={'class': 'form-select'})
        }
