from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("checkout/<int:product_id>/", views.checkout, name='checkout'),
    path("payment-success/<int:product_id>/", views.payment_successful, name='success'),
    path("payment-failed/<int:product_id>", views.payment_failed, name='failed')
]