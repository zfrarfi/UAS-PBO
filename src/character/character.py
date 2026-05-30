import pygame

class Character:
    def __init__(self, x_position, y_position, name, bubble_chat,speed):
        self.x_position = x_position
        self.y_position = y_position
        self.name = name
        self.bubble_chat = bubble_chat
        self.speed = speed
        self.image = None
        self.rect = pygame.Rect(x_position, y_position,100, 100)
        
    def move (self, dx, dy):
        self.x_position += dx
        self.y_position += dy
        self.rect.center = (self.x_position, self.y_position)
        
    def draw(self, surface, offset=(0, 0)):
        if self.image:
            draw_rect = self.rect.move(-offset[0], -offset[1])
            surface.blit(self.image, draw_rect)