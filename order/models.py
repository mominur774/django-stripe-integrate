from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Pricing(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    pricing = models.ForeignKey(
        Pricing,
        on_delete=models.CASCADE
    )
    amount = models.FloatField()
    address = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}'s order"
