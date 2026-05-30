import os
import pygame
import sys
from character_ygngerjain.barista import Barista
from character_ygngerjain.customer import Customer
from ui_ygngerjain.mainmenu import MainMenu
from environtment_taqiy.camera import CameraManager
from ui_ygngerjain.dialog import DialogueManager
from menu_ygngerjain.order_menu import OrderMenu
from ui_ygngerjain.hud import Hud
from ui_ygngerjain.kitchen import KitchenMode
from order_system.orders import OrderManager
pygame.init()

WIDTH = 1280
HEIGHT = 720

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
MAP_PATH = os.path.join(BASE_DIR, "assets", "image", "map", "mapcafe.png")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midnight Cafe")

CASHIER_BG_PATH = os.path.join(BASE_DIR, "D:/Vs Code/UAS-PBO/assets/image/map/lantai_luas.png")
cashier_bg = pygame.image.load(CASHIER_BG_PATH).convert_alpha()
cashier_bg = pygame.transform.smoothscale(cashier_bg, (WIDTH, HEIGHT))

bg_img = pygame.image.load(MAP_PATH).convert_alpha()
BG_WIDTH, BG_HEIGHT = bg_img.get_size()
bg_menu = pygame.transform.smoothscale(bg_img, (WIDTH, HEIGHT))

barista = Barista(WIDTH // 2, HEIGHT // 2)

customer = Customer(
    x_position=BG_WIDTH - 50,
    y_position=400   
)
print("Customer berhasil dibuat")

dialogue_manager = DialogueManager()
camera_manager = CameraManager()
order_menu = OrderMenu()

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
                        # tes 
                    elif event.key == pygame.K_e:
                        jarak_x = abs(barista.x_position - customer.x_position)
                        jarak_y = abs(barista.y_position - customer.y_position)
                        if jarak_x < 80 and jarak_y < 80 and customer.state == "ordering":
                            game_state = "dialogue"
                            dialogue_manager.start([
                                {"speaker": "Barista", "text": "Halo, mau pesan apa?"},
                                {"speaker": "Customer", "text": "Boleh lihat menunya?"},
                            ])
                    elif pygame.K_1 <= event.key <= pygame.K_9:
                        idx = event.key - pygame.K_1
                        price = order_manager.complete_order(idx)
                        if price > 0:
                            hud.add_money(price)

            elif game_state == "kitchen":
                kitchen_action = kitchen_mode.handle_event(event)
                if kitchen_action == "exit":
                    game_state = "world"
            
            elif game_state == "dialogue":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        dialogue_manager.next()
                        if not dialogue_manager.is_active:
                            game_state = "world"
                            camera_manager.set_target(0, 0, "normal")

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
            camera_manager.update()
            hud.update(dt)
            order_manager.update()

            camera_x = clamp(barista.x_position - WIDTH // 2, 0, max(0, BG_WIDTH - WIDTH))
            camera_y = clamp(barista.y_position - HEIGHT // 2, 0, max(0, BG_HEIGHT - HEIGHT))
            screen.blit(bg_img, (0, 0), (camera_x, camera_y, WIDTH, HEIGHT))
            customer.draw(screen, (camera_x, camera_y))
            barista.draw(screen, (camera_x, camera_y))

# tes 
            jarak_x = abs(barista.x_position - customer.x_position)
            jarak_y = abs(barista.y_position - customer.y_position)

            if jarak_x < 80 and jarak_y < 80 and customer.state == "ordering":
                prompt_e = pygame.font.Font(None, 28).render(
                    "Tekan E untuk terima pesanan", True, (255, 255, 255)
                )
                screen.blit(prompt_e, (WIDTH // 2 - 150, HEIGHT - 80))

            prompt = "Press K to enter kitchen mode"
            prompt_surf = pygame.font.Font(None, 28).render(prompt, True, (255, 240, 200))
            screen.blit(prompt_surf, (20, HEIGHT - 40))

            hud.draw(screen)
        elif game_state == "kitchen":
            kitchen_mode.draw(screen)
            
        elif game_state == "dialogue":
            screen.blit(cashier_bg, (0, 0))
            customer_img = customer.get_current_image()
            screen.blit(customer_img,(WIDTH // 2 - 50, HEIGHT // 2 - 150))
            dialogue_manager.draw(screen)
    else:
        screen.blit(bg_menu, (0, 0))
        main_menu.draw(screen)

    pygame.display.update()

pygame.quit()
sys.exit()

