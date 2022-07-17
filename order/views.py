from django.shortcuts import redirect, render
from order.models import Pricing
from order.models import Order
from django.conf import settings
from payment.models import Payment
from django.contrib.auth.decorators import login_required

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.


def pricing_list(request):
    pricing = Pricing.objects.all()

    context = {
        'pricing': pricing
    }
    return render(request, 'order/pricing_list.html', context)


@login_required
def pricing_details(request, id):
    pricing = Pricing.objects.get(id=id)
    if request.method == 'POST':
        address = request.POST.get('address')

        order = Order.objects.create(
            user=request.user,
            pricing=pricing,
            amount=pricing.price,
            address=address
        )

        # create payment intent
        payment_intent = stripe.PaymentIntent.create(
            amount=int(order.amount) * 100,
            currency="usd",
            payment_method_types=["card"],
            receipt_email=request.user.email
        )
        # create payment
        payment = Payment.objects.create(
            user=request.user,
            order=order,
            total_amount=int(order.amount) * 100,
            stripe_response=payment_intent,
            payment_intent_id=payment_intent['id']
        )

        request.session['client_secret'] = payment.stripe_response['client_secret']
        request.session['stripe_pk'] = settings.STRIPE_PUBLISHABLE_KEY
        request.session['intent_id'] = payment.payment_intent_id

        return redirect('/payment/checkout')

    context = {
        'pricing': pricing
    }
    return render(request, 'order/pricing_details.html', context)
