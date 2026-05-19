import pygame
import sys

pygame.init()
monitor_info = pygame.display.Info()

WIDTH = monitor_info.current_w
HEIGHT = monitor_info.current_h

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midnight Cafe")
bg_img = pygame.image.load(r"C:\Users\fauza\Tugas Matkul\semster 2\pbo\Project akhir github\UAS-PBO\assets\image\map\map_lengkap.jpeg")
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