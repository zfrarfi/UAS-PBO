import pygame
import sys
from character_ygngerjain.barista import Barista

pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midnight Cafe")
bg_img = pygame.image.load("D:/Vs Code/UAS-PBO/assets/image/map/mapcafe.png")
bg_scaled = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))

barista = Barista(WIDTH // 2, HEIGHT // 2)
running = True
#SLDKJWEDGFNEIBF
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    barista.input()

    screen.blit(bg_scaled,(0, 0))
    barista.draw(screen)
    pygame.display.update()

pygame.quit()
sys.exit()
# alkfjalkdsjfl