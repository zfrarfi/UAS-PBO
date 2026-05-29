import pygame
from character_ygngerjain.character import Character

class Barista(Character):
    def __init__(self,x_position, y_position,):
        super().__init__(x_position,y_position,speed = 0.5,name = "Barista", bubble_chat="")
        
        self.front = pygame.image.load("D:/Vs Code/UAS-PBO/assets/image/character/barista/barista_back.png").convert_alpha()
        self.back = pygame.image.load("D:/Vs Code/UAS-PBO/assets/image/character/barista/barista_front.png").convert_alpha()
        self.left = pygame.image.load("D:/Vs Code/UAS-PBO/assets/image/character/barista/barista_left.png").convert_alpha()
        self.right = pygame.image.load("D:/Vs Code/UAS-PBO/assets/image/character/barista/barista_right.png").convert_alpha()
        
        self.front = pygame.transform.scale(self.front, (100, 100))
        self.back = pygame.transform.scale(self.back, (100, 100))
        self.left = pygame.transform.scale(self.left, (100, 100))
        self.right = pygame.transform.scale(self.right, (100, 100))
        
        self.image = self.front
        
    def input(self):
        keys = pygame.key.get_pressed()
        dx = 0
        dy = 0
        
        if keys[pygame.K_a]:
            dx = -self.speed
            self.image = self.left

        if keys[pygame.K_d]:
            dx = self.speed
            self.image = self.right

        if keys[pygame.K_w]:
            dy = -self.speed
            self.image = self.back

        if keys[pygame.K_s]:
            dy = self.speed
            self.image = self.front

        self.move(dx, dy)