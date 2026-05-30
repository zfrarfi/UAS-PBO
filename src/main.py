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

    WIDTH = 1280
    HEIGHT = 720

    screen = pygame.display.set_mode(
        (WIDTH, HEIGHT)
    )

    pygame.display.set_caption(
        "Midnight Cafe"
    )

    clock = pygame.time.Clock()

    # Environment
    map_cafe = MapCafe()

    # Character
    barista = Barista(
        WIDTH // 2,
        HEIGHT // 2
    )

    customer = Customer(
        x_position=WIDTH - 50,
        y_position=400
    )

    # UI
    main_menu = MainMenu(
        WIDTH,
        HEIGHT
    )

    order_manager = OrderManager()

    hud = Hud(
        barista=barista,
        order_manager=order_manager,
        start_money=0
    )

    kitchen_mode = KitchenMode(
        WIDTH,
        HEIGHT,
        order_manager,
        hud
    )

    running = True

    game_state = "world"

    while running:

        dt = clock.tick(60) / 1000

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            menu_action = main_menu.handle_event(
                event
            )

            if menu_action == "Quit":
                running = False

            elif menu_action == "Start":
                main_menu.active = False

            if not main_menu.active:

                if game_state == "world":

                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_k:
                            game_state = "kitchen"

                elif game_state == "kitchen":

                    result = kitchen_mode.handle_event(
                        event
                    )

                    if result == "exit":
                        game_state = "world"

        # UPDATE

        if not main_menu.active:

            if game_state == "world":

                barista.input(dt)

                customer.update()

                hud.update(dt)

                order_manager.update()

        # DRAW

        screen.fill((0, 0, 0))

        if main_menu.active:

            main_menu.draw(screen)

        else:

            if game_state == "world":

                map_cafe.gambarMap(screen)

                customer.draw(screen, (0, 0))

                barista.draw(screen, (0, 0))

                # DEBUG COLLISION
                for hitbox in map_cafe.get_collisions():

                    pygame.draw.rect(
                        screen,
                        (255, 0, 0),
                        hitbox,
                        2
                    )

                hud.draw(screen)

            elif game_state == "kitchen":

                kitchen_mode.draw(screen)

        pygame.display.flip()

    pygame.quit()

    sys.exit()


if __name__ == "__main__":
    main()