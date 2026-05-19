import pygame
import sys

pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midnight Cafe")
bg_img = pygame.image.load("../assets/image/map/map_lengkap.jpeg")
bg_scaled = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))
running = True
#SLDKJWEDGFNEIBF
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg_scaled,(0, 0))
    pygame.display.update()

pygame.quit()
sys.exit()

