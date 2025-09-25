from django import forms
from .models import Availability, UserProfile
from .models import Profile
from .models import Golfer
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


class FavoriteGolferForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['favorite_golfers']
        widgets = {
            'favorite_golfers': forms.CheckboxSelectMultiple
        }