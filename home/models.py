from django.db import models
from django.contrib.auth.models import User

class Availability(models.Model):
    TIME_SLOTS = [
        ("sat_5pm", "Saturday 5 PM"),
        ("sun_9am", "Sunday 9 AM"),
        ("sun_11am", "Sunday 11 AM"),
        ("sun_6pm", "Sunday 6 PM"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    time_slot = models.CharField(max_length=20, choices=TIME_SLOTS, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_time_slot_display() if self.time_slot else 'No Availability'}"


class Profile(models.Model):
    TEAMS = [
        ("wf", "wake forest"),
        ("unc", "north carolina"),
        ("fau", "flordia atlantic"),
        ("wvu", "west virgina"),
        ("uf", "flordia"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_team = models.CharField(max_length=3, choices=TEAMS, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_favorite_team_display() if self.favorite_team else 'No Team'}"
