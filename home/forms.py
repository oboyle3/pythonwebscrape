from django import forms
from .models import Availability
from .models import Profile
class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['time_slot']
        widgets = {
            'time_slot': forms.Select(attrs={'class': 'form-select'})
        }




class TeamForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["favorite_team"]
