import random
import time

class Order:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.created = time.time()

class OrderManager:
    """Simple order manager: spawn orders periodically and allow completing them."""
    SAMPLE_MENU = [
        ("Coffee", 5),
        ("Tea", 4),
        ("Cake", 7),
        ("Sandwich", 8),
        ("Juice", 6),
    ]

    def __init__(self):
        self.orders = []
        self.last_spawn = time.time()
        self.spawn_interval = 8.0

    def update(self):
        now = time.time()
        if now - self.last_spawn >= self.spawn_interval:
            self.spawn_order()
            self.last_spawn = now

    def spawn_order(self):
        name, price = random.choice(self.SAMPLE_MENU)
        self.orders.append(Order(name, price))

    def complete_order(self, index):
        if 0 <= index < len(self.orders):
            order = self.orders.pop(index)
            return order.price
        return 0

    def get_orders(self):
        return list(self.orders)
