from django.contrib import admin
from payment.models import Payment

# Register your models here.

# admin.site.register(Payment)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'stripe_response',
                    'payment_intent_id', 'payment_succeeded', 'total_amount']
