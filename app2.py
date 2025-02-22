from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection details
db_config = {
    'host': 'localhost',  # Usually 'localhost' on GoDaddy
    'user': 'french_user',  # Your database username
    'password': 'your_password',  # Your database password
    'database': 'french_course_subscriptions'  # Your database name
}

# Function to connect to the database
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Route to handle subscription
@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.json
    plan = data.get('plan')
    user_id = data.get('user_id')
    payment_amount = data.get('payment_amount')
    transaction_id = data.get('transaction_id')

    if not all([plan, user_id, payment_amount, transaction_id]):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert into the appropriate table
        if plan == 'monthly':
            query = """
            INSERT INTO monthly_subscriptions (user_id, subscription_date, payment_status, payment_amount, payment_gateway_transaction_id)
            VALUES (%s, NOW(), 'pending', %s, %s)
            """
        elif plan == 'yearly':
            query = """
            INSERT INTO yearly_subscriptions (user_id, subscription_date, payment_status, payment_amount, payment_gateway_transaction_id)
            VALUES (%s, NOW(), 'pending', %s, %s)
            """
        elif plan == 'coaching':
            query = """
            INSERT INTO coaching_subscriptions (user_id, subscription_date, payment_status, payment_amount, payment_gateway_transaction_id)
            VALUES (%s, NOW(), 'pending', %s, %s)
            """
        else:
            return jsonify({'error': 'Invalid plan'}), 400

        cursor.execute(query, (user_id, payment_amount, transaction_id))
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({'message': 'Subscription successful!'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)