import pygame
import sys

pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midnight Cafe")
bg_img = pygame.image.load("D:/Vs Code/UAS PBO/assets/image/map/lantai_luas.png")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg_img,(0, 0))
    pygame.display.update()

pygame.quit()
sys.exit()

