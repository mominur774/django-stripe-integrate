from django.db import models
from django.contrib.auth.models import User

from order.models import Order

# Create your models here.


class Payment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )
    stripe_response = models.JSONField(null=True, blank=True)
    payment_intent_id = models.CharField(max_length=255)
    payment_succeeded = models.BooleanField(default=False)
    total_amount = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}'s payment"
