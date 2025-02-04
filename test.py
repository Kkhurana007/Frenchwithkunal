import stripe

stripe.api_key = 'pk_live_51OVgS8KoApplm6wZeLZNXNznTBTsu1oArI7OVynmo7k4I4V18gcjpWurGy2oKphzGxFhqHRmciStv2F1lMdt9RJZ00alfydkwz'

# Create a product
product = stripe.Product.create(
    name="French Course Monthly Plan",
    description="Access to all lessons, new content every week."
)

# Create a price for the product
price = stripe.Price.create(
    unit_amount=5000,  # $50.00 in cents
    currency="usd",
    recurring={"interval": "month"},
    product=product.id,
)

print("Price ID:", price.id)