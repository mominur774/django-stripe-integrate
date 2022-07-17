from django.shortcuts import redirect, render
from django.contrib import messages
from payment.models import Payment

# Create your views here.


def checkout(request):
    return render(request, 'payment/checkout.html')


def payment_succeeded(request, intent_id):
    payment = Payment.objects.get(
        user=request.user, payment_intent_id=intent_id)
    payment.payment_succeeded = True
    payment.save()
    messages.success(request, 'Payment successfull!')
    return redirect('/')
