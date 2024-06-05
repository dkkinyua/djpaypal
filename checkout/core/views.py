from django.shortcuts import render
from .models import Product
from django.

# Create your views here.
def index(request):
    context = {
        "products": Product.objects.all()
    }

    return render(request, "core/index.html", context)

def checkout(request, product_id):
    product = Product.objects.get(pk=product_id)

    context = {
        "product": product
    }

    return render(request, "core/checkout.html", context)

def payment_successful(request, product_id):
    product = Product.objects.get(pk=product_id)

    return render(request, "core/payment_successful.html", {"product": product})

def payment_failed(request, product_id):
    product = Product.objects.get(pk=product_id)

    return render(request, "core/payment_failed.html", {"product": product})