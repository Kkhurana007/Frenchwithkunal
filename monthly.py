from flask import Flask, jsonify, request
import stripe

from flask_cors import CORS



app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Set your secret key
stripe.api_key = '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'

@app.route('/create-checkout-session-monthly', methods=['POST'])
def create_checkout_session_monthly():
    try:
        # Create a Stripe Checkout Session for the monthly plan
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': 'req_LosajFhR9RW9xy',  # Replace with your price ID
                'quantity': 1,
            }],
            mode='subscription',
            success_url='https://frenchwithkunal.ca/success',  # Replace with your success URL
            cancel_url='https://frenchwithkunal.ca/cancel',    # Replace with your cancel URL
        )
        return jsonify({'id': session.id})
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/create-checkout-session-yearly', methods=['POST'])
def create_checkout_session_yearly():
    try:
        # Create a Stripe Checkout Session for the yearly plan
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': 'prod_RiHMDvtNc58RBdd',  # Replace with your price ID
                'quantity': 1,
            }],
            mode='subscription',
            success_url='https://yourwebsite.com/success',  # Replace with your success URL
            cancel_url='https://yourwebsite.com/cancel',    # Replace with your cancel URL
        )
        return jsonify({'id': session.id})
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)