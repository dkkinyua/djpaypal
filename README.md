# Django PayPal Integration

This Django application demonstrates integration with PayPal for handling payments. It provides endpoints for initiating payments, handling successful and failed payments, and more. You will need two Paypal accounts, a business and personal account. The business account is for receiving payment *(merchant)* and the personal account is for sending out payments *(customer)*.

To open a test merchant account, go to *https://sandbox.paypal.com* and select the *'Business Account'* to create one.
to create a test personal account, go to *https://sandbox.paypal.com* and select the *'Personal Account'* to create one.

## Procedure

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/djpaypal.git
   cd djpaypal

2. Create a virtual environment, I use virtualenv but feel free to use the virtual environment of your choice:
```bash
bash

virtualenv env
source env/bin/activate

```
This creates a ```env``` folder in your directory

3. Download necessary packages and modules:
In the cloned directory, there is a requirements.txt file, a file that contains all the necessary modules and packages required for this project e.g. ```django-paypal```, ```django``` among others. To install them, run:

```bash
bash

pip install -r requirements.txt

```
4. After installing all the requirements, cd to the checkout/ directory and run the Djnago server which will run on *localhost:8000*. To do so, run the following command:
```bash
bash

cd checkout
python manage.py runserver

```

You will or might get a *Unapplied migrations error* while running the server. To fix this error, run:

```bash
bash

python manage.py migrate
python manage.py runserver


```
This will fix the *Unapplied migrations error*.

5. In settings.py, add the following configuration settings for Paypal:
```python

checkout/settings.py
import os
from dotenv import load_dotenv

load_dotenv()

... # Other settings and configs

PAYPAL_RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL') # The merchant account email address
PAYPAL_TEST = True

```
**CAUTION: Always store your sensitive information like emails and passwords inside of a .env folder and import them using ```python-dotenv``` or ```python-decouple``` as shown above.**

6. In views.py, initialize a host URL using the ```request.get_host()``` method and create a dictionary called paypal_checkout (Call these variables as you like!):
```python

core/views.py

from .models import Product
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.urls import reverse
import uuid

# Other views
def checkout(request, product_id):
    product = Product.objects.get(id=product_id)

    host = request.get_host()

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': product.price,
        'item_name': product.title,
        'currency_code': 'USD',
        'notify_url': f'http://{host}{reverse('paypal-ipn')}',
        'return_url': f'http://{host}{reverse('core:payment-success', kwargs={'product_id': product.id})}',
        'cancel_url': f'http://{host}{reverse('core:payment-failed', kwargs={'product_id': product.id})}',
    }

```
7. After creating the above dictionary, create a variable paypal_payment. This variable automatically loads the paypal_checkout dictionary into a form which is PayPalPaymentsForm. Add the paypal_payment variable into the context dictionary to render it to the frontend.

```python

core/views.py

paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

context = {
    'product': product,
    'paypal': paypal_payment
}

```
8. Go to *localhost:8000/checkout/<product_id>* to check if it works!

**Endpoints and Descriptions**
| Endpoint    | Description |
| ----------- | ----------- |
| 1. 'checkout/<int:product_id>'   | This URL endpoint directs the user to the 'checkout' page|
| 2. 'payment-success/<int:product_id>'   |This URL endpoint is triggered when payment is successful|
| 3. 'payment-failed/<int:product_id>'   | This URL endpoint is when a payment process fails|
| 4. '/'   | Index page of the website|

# Feel free to clone this project, contribute to it too!
