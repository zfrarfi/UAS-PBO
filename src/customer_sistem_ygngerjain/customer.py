from character_sistem_ygngerjain.character import Character

class Customer(Character):
    def __init__(self, x_position, y_position, name, bubble_chat, money):
        super().__init__(x_position, y_position, name, bubble_chat)
        self.money = money