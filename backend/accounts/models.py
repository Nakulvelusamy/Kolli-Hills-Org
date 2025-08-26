from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=20, default='user')

    def __str__(self):
        return self.email
