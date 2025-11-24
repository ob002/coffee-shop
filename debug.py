from customer import Customer
from coffee import Coffee
from order import Order

# Create customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create orders
alice.create_order(latte, 5.5)
alice.create_order(latte, 6.0)
bob.create_order(latte, 5.0)
bob.create_order(espresso, 4.0)

# Test relationships
print("Alice's coffees:", [c.name for c in alice.coffees()])
print("Latte orders:", len(latte.orders()))
print("Latte customers:", [c.name for c in latte.customers()])
print("Latte avg price:", latte.average_price())

# Test most aficionado
aficionado = Customer.most_aficionado(latte)
print("Biggest latte fan:", aficionado.name if aficionado else "None")