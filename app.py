```  
from flask import Flask, request, jsonify import stripe

app = Flask(**name**) stripe.api_key = 'sk_test_XXXXXXXXXXXXXXXXXXXXXXXX' \# Your Stripe Secret Key

@app.route('/create-checkout-session', methods=\['POST'\]) def create_checkout_session(): data = request.get_json() plan = data.get('plan') \# 'monthly' or 'yearly'

```         
try:
    if plan == 'monthly':
        price_data = {
            'currency': 'usd',
            'product_data': {
                'name': 'Abonnement Mensuel au cours de français',
            },
            'unit_amount': 5000,  # $50.00 (in cents)
        }
    elif plan == 'yearly':
        price_data = {
            'currency': 'usd',
            'product_data': {
                'name': 'Abonnement Annuel au cours de français',
            },
            'unit_amount': 45000,  # $450.00 (in cents)
        }
    else:
        return jsonify({'error': 'Plan invalide'}), 400

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': price_data,
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:5000/success',
        cancel_url='http://localhost:5000/cancel',
    )
    return jsonify({'id': checkout_session.id})
except Exception as e:
    return str(e), 400
```

if **name** == '**main**': app.run(debug=True)
```
