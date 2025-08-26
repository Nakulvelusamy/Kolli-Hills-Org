from django.db import models
from accounts.models import User

class ContactTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    status = models.CharField(max_length=20, default='open')

    def __str__(self):
        return f"Ticket from {self.user.email}"
