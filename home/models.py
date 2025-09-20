from django.db import models


from django.contrib.auth.models import User

class Availability(models.Model):
    WEEKEND_TIMES = [
        ('sat_5pm', 'Saturday 5 PM'),
        ('sun_9am', 'Sunday 9 AM'),
        ('sun_11am', 'Sunday 11 AM'),
        ('sun_6pm', 'Sunday 6 PM'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_slot = models.CharField(max_length=20, choices=WEEKEND_TIMES)

    def __str__(self):
        return f"{self.user.username} - {self.get_time_slot_display()}"
