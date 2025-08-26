from django.db import models
from accounts.models import User
from products.models import Product

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"Wishlist of {self.user.email}"
