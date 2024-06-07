from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path("", views.index, name='index'),
    path("checkout/<int:product_id>/", views.checkout, name='checkout'),
    path("payment-success/<int:product_id>/", views.payment_successful, name='payment-success'),
    path("payment-failed/<int:product_id>/", views.payment_failed, name='payment-failed')
]