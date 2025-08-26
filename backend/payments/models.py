from django.db import models
from accounts.models import User

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f"Payment by {self.user.email}"
