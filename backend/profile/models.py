from django.db import models
from accounts.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    loyalty_points = models.IntegerField(default=0)
    subscription_active = models.BooleanField(default=False)

    def __str__(self):
        return f"Profile of {self.user.email}"
