from character_sistem_ygngerjain.character import Character

class Barista(Character):
    def __init__(self, x_position, y_position, name, bubble_chat, money, saldo):
        super().__init__(x_position, y_position, name, bubble_chat)

        self.money = money
        self.saldo = saldo
