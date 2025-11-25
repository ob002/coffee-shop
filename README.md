# coffee-shop
A Python object-oriented implementation modeling a coffee shop domain with customers, coffees, and orders.

## 📁 Project Structure

```
coffee_shop/
├── customer.py       # Customer class
├── coffee.py         # Coffee class
├── order.py          # Order class (central linking entity)
├── debug.py          # Interactive demo script

```

## 🧩 Domain Relationships

- A **Customer** can place many **Orders**.
- A **Coffee** can have many **Orders**.
- An **Order** belongs to exactly **one Customer** and **one Coffee**.
- This creates a **many-to-many relationship** between `Customer` and `Coffee` via `Order`.

## 🚀 Features

### ✅ Validation & Safety
- `Customer.name`: string, 1–15 characters
- `Coffee.name`: string, at least 3 characters
- `Order.price`: float between 1.0 and 10.0
- Type validation for all relationships

### 🔗 Relationship Navigation
- `customer.orders()` → list of Order objects
- `customer.coffees()` → unique list of Coffee objects
- `coffee.orders()` → list of Order objects
- `coffee.customers()` → unique list of Customer objects

### 📊 Business Logic
- `customer.create_order(coffee, price)` → creates and links a new order
- `coffee.num_orders()` → total orders for a coffee
- `coffee.average_price()` → average price across all orders
- `Customer.most_aficionado(coffee)` → returns customer who spent the most on a given coffee

### 🧪 No Circular Imports
- Uses class-level registry (`Order.all`) as single source of truth
- Avoids top-level circular dependencies by validating types via duck typing

---

## 🛠️ Setup & Usage

### 1. Clone or navigate to the project directory
```bash
cd coffee-shop
```

### 2. Run the demo
```bash
python debug.py
```

Example output:
```
Arthur's coffees: ['Latte']
 black coffee orders: 3
black coffee customers: ['Arthur', 'Willy']
black coffee average price: 5.5
Biggest black coffee fan: Arthur
```

## 📜 Example Code

```python
from customer import Customer
from coffee import Coffee

# Create entities
arthur = Customer("Arthur")
black coffee = Coffee("CBlack Coffee")

# Place an order
arthur.create_order(black coffee, 4.75)

# Explore relationships
print(f"{arthur.name} ordered: {[c.name for c in arthur.coffees()]}")
print(f"'{black coffee.name}' has {black coffee.num_orders()} orders")
```

---

## 📎 Design Notes

- **Single Source of Truth**: All `Order` instances are tracked in `Order.all`
- **Encapsulation**: Properties enforce data integrity via setters
- **Efficiency**: Uses sets to ensure unique customers/coffees in relationship lists
- **Scalability**: Easy to extend (e.g., add timestamps, order status, etc.)

---

## 📝 Author

keypoints for whats needed
- Class design
- Inheritance-free composition
- Bidirectional relationships
- Aggregate data computation

