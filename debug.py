from customer import Customer
from coffee import Coffee
from order import Order

# Create customers
arthur = Customer("Arthur")
willy = Customer("Willy")

# Create coffees
blackcoffee = Coffee("Black Coffee")
whitecoffee = Coffee("white Coffee")

# Create orders
arthur.create_order(blackcoffee, 5.5)
arthur.create_order(blackcoffee, 6.0)
willy.create_order(blackcoffee, 5.0)
willy.create_order(whitecoffee, 4.0)

# Test relationships
print("Arthur's coffees:", [c.name for c in arthur.coffees()])
print("Black Coffee orders:", len(blackcoffee.orders()))
print("Black Coffee customers:", [c.name for c in blackcoffee.customers()])
print("Black Coffee avg price:", blackcoffee.average_price())

# Test most aficionado
aficionado = Customer.most_aficionado(blackcoffee)
print("Biggest black coffee fan:", aficionado.name if aficionado else "None")