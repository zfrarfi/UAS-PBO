from abc import ABC        
import pygame
import sys

pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midnight Cafe")

class Menu(ABC):
    def __init__(self, nama, harga, bahan):
        self.nama = nama
        self.harga = harga
        self.bahan = bahan
        
class Minuman(Menu):
    def __init__(self, nama, harga, bahan):
        super().__init__(nama, harga, bahan)
        
class Makanan(Menu):
    def __init__(self, nama, harga, bahan):
        super().__init__(nama, harga, bahan)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((67, 67, 67))
    pygame.display.update()

pygame.quit()
sys.exit()

