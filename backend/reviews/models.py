from django.db import models
from accounts.models import User
from products.models import Product

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    image = models.ImageField(upload_to='review_images/', null=True, blank=True)

    def __str__(self):
        return f"Review by {self.user.email}"
