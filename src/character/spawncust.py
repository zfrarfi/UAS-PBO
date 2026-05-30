from character.customer import Customer
import random

class SpawnCust:
    def __init__(self):
        self.customers = []
        self.spawn_timer = 0
        self.spawn_delay = 300

    def spawn_customer(self):
        x_position = random.randint(50, 200)
        y_position = random.randint(50, 600)

        customer = Customer(x_position, y_position)

        self.customers.append(customer)

    def update(self):
        self.spawn_timer += 1

        if self.spawn_timer >= self.spawn_delay:
            self.spawn_customer()
            self.spawn_timer = 0

        for customer in self.customers:
            customer.update()

    def draw(self, surface):
        for customer in self.customers:
            customer.draw(surface)