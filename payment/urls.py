from django.urls import path
from payment import views

urlpatterns = [
    path('checkout/', views.checkout, name="checkout"),
    path('payment-succeeded/<intent_id>/',
         views.payment_succeeded, name="payment-succeeded"),
]
