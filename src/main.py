import os
import pygame
import sys
from character_ygngerjain.barista import Barista
from ui_ygngerjain.mainmenu import MainMenu
pygame.init()

WIDTH = 1280
HEIGHT = 720

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
MAP_PATH = os.path.join(BASE_DIR, "assets", "image", "map", "mapcafe.png")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midnight Cafe")
bg_img = pygame.image.load(MAP_PATH)
bg_scaled = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))

barista = Barista(WIDTH // 2, HEIGHT // 2)
main_menu = MainMenu(WIDTH, HEIGHT)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        menu_action = main_menu.handle_event(event)
        if menu_action == "Quit":
            running = False
        elif menu_action == "Start":
            main_menu.active = False
            main_menu.set_status("")
        elif menu_action in ("Load", "Preferences", "Help", "About"):
            main_menu.show_option(menu_action)

    if not main_menu.active:
        barista.input()

    screen.blit(bg_scaled, (0, 0))
    barista.draw(screen)
    if main_menu.active:
        main_menu.draw(screen)
    pygame.display.update()

pygame.quit()
sys.exit()

