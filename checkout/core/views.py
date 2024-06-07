from django.shortcuts import render
from .models import Product
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.urls import reverse
import uuid


# Create your views here.
def index(request):
    context = {
        "products": Product.objects.all()
    }

    return render(request, "core/index.html", context)

def checkout(request, product_id):
    product = Product.objects.get(pk=product_id)

    host = request.get_host()

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': product.price,
        'item_name': product.title,
        'invoice': str(uuid.uuid4()), # Creates a unique ID
        'currency_code': 'USD',
        'notify_url': f'http://{host}{reverse('paypal-ipn')}',
        'return_url': f'http://{host}{reverse('core:payment-success', kwargs={'product_id': product.id})}',
        'cancel_url': f'http://{host}{reverse('core:payment-failed', kwargs={'product_id': product.id})}',
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

    context = {
        "product": product,
        "paypal": paypal_payment
    }

    return render(request, "core/checkout.html", context)

def payment_successful(request, product_id):
    product = Product.objects.get(id=product_id)

    return render(request, "core/payment_successful.html", {"product": product})

def payment_failed(request, product_id):
    product = Product.objects.get(id=product_id)

    return render(request, "core/payment_failed.html", {"product": product})