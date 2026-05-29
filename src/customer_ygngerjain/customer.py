import pygame
from character_ygngerjain.character import Character

class Customer(Character):
    def __init__(self, x_position, y_position, name, bubble_chat, money):
        super().__init__(x_position, y_position, name = "Cuustomer", bubble_chat = ", speed = 0.5")
        self.money = money
        
        self.image = pygame.image.load("").convert_alpha()
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect(center=(x_position, y_position))
        
    def update(self):
        self.x_position += self.speed
        self.rect.center = (self.x_position,self.y_position)