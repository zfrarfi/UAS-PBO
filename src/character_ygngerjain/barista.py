import os
import pygame
from character_ygngerjain.character import Character

class Barista(Character):
    def __init__(self,x_position, y_position,):
        super().__init__(x_position,y_position,speed = 0.5,name = "Barista", bubble_chat="")

        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
        character_dir = os.path.join(base_dir, "assets", "image", "character", "barista")

        def load_scaled(filename, width=100):
            image = pygame.image.load(os.path.join(character_dir, filename)).convert_alpha()
            scale = width / image.get_width()
            new_height = max(1, int(image.get_height() * scale))
            return pygame.transform.smoothscale(image, (width, new_height))

        self.front = load_scaled("barista_back.png")
        self.back = load_scaled("barista_front.png")
        self.left = load_scaled("barista_left.png")
        self.right = load_scaled("barista_right.png")

        self.image = self.front
        self.rect = self.image.get_rect(center=(x_position, y_position))
        
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