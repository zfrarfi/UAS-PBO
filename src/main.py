import os
import pygame
import sys
from environment_taqiy.mapcafe import MapCafe

from character_ygngerjain.barista import Barista
from character_ygngerjain.customer import Customer
from ui_ygngerjain.mainmenu import MainMenu
from ui_ygngerjain.hud import Hud
from ui_ygngerjain.kitchen import KitchenMode
from order_system.orders import OrderManager

def main():
    pygame.init()

    # Ukuran jendela game (Sesuaikan jika resolusi gambar lantai berbeda)
    WIDTH, HEIGHT = 1280, 720
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Midnight Cafe - Environment Area (King Fauzan Paduka)")

    clock = pygame.time.Clock()

    # HANYA meload sistem Map dan Furniture
    map_cafe = MapCafe(0, 0)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
MAP_PATH = os.path.join(BASE_DIR, "assets", "image", "map", "mapcafe.png")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midnight Cafe")
bg_img = pygame.image.load(MAP_PATH).convert_alpha()
BG_WIDTH, BG_HEIGHT = bg_img.get_size()
bg_menu = pygame.transform.smoothscale(bg_img, (WIDTH, HEIGHT))

barista = Barista(WIDTH // 2, HEIGHT // 2)

customer = Customer(
    x_position=BG_WIDTH - 50,
    y_position=400   
)
print("Customer berhasil dibuat")
main_menu = MainMenu(WIDTH, HEIGHT)
order_manager = OrderManager()
hud = Hud(barista=barista, order_manager=order_manager, start_money=0)
kitchen_mode = KitchenMode(WIDTH, HEIGHT, order_manager, hud)
clock = pygame.time.Clock()
running = True
game_state = "world"

def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))

while running:
    dt = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not main_menu.active:
            if game_state == "world":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_k:
                        game_state = "kitchen"
                    elif pygame.K_1 <= event.key <= pygame.K_9:
                        idx = event.key - pygame.K_1
                        price = order_manager.complete_order(idx)
                        if price > 0:
                            hud.add_money(price)

            elif game_state == "kitchen":
                kitchen_action = kitchen_mode.handle_event(event)
                if kitchen_action == "exit":
                    game_state = "world"

        menu_action = main_menu.handle_event(event)
        if menu_action == "Quit":
            running = False
        elif menu_action == "Start":
            main_menu.active = False
            main_menu.set_status("")
        elif menu_action in ("Load", "Preferences", "Help", "About"):
            main_menu.show_option(menu_action)

    if not main_menu.active:
        if game_state == "world":
            barista.input(dt)
            customer.update()
            hud.update(dt)
            order_manager.update()

            camera_x = clamp(barista.x_position - WIDTH // 2, 0, max(0, BG_WIDTH - WIDTH))
            camera_y = clamp(barista.y_position - HEIGHT // 2, 0, max(0, BG_HEIGHT - HEIGHT))
            screen.blit(bg_img, (0, 0), (camera_x, camera_y, WIDTH, HEIGHT))
            customer.draw(screen, (camera_x, camera_y))
            barista.draw(screen, (camera_x, camera_y))

            prompt = "Press K to enter kitchen mode"
            prompt_surf = pygame.font.Font(None, 28).render(prompt, True, (255, 240, 200))
            screen.blit(prompt_surf, (20, HEIGHT - 40))

            hud.draw(screen)
        elif game_state == "kitchen":
            kitchen_mode.draw(screen)
    else:
        screen.blit(bg_menu, (0, 0))
        main_menu.draw(screen)

    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Bersihkan layar tiap frame
        screen.fill((0, 0, 0))

        # Render semua tata letak cafe
        map_cafe.gambarMap(screen)

        # ========================================================
        # MODE DEBUG: Menampilkan garis merah untuk mengecek tabrakan
        # Sangat berguna untuk kalibrasi koordinat X dan Y perabotan
        # ========================================================
        for hitbox in map_cafe.get_collisions():
            pygame.draw.rect(screen, (255, 0, 0), hitbox, 2)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()