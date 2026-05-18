class Character:
    def __init__(self, x_position, y_position, name, bubble_chat):
        self.x_position = x_position
        self.y_position = y_position
        self.name = name
        self.bubble_chat = bubble_chat  
        
class Customer(Character):
    def __init__(self, x_position, y_position, name, bubble_chat, money):
        super().__init__(x_position, y_position, name, bubble_chat)
        self.money = money
        
class Barista(Character):
    def __init__(self, x_position, y_position, name, bubble_chat, money, saldo):
        super().__init__(x_position, y_position, name, bubble_chat)

        self.money = money
        self.saldo = saldo
        
class spawnCust():
    def __init__(self, customerList, maxCustomer):
        self.customerList = customerList
        self.maxCustomer = maxCustomer