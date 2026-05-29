import os
import pygame

class KitchenMode:
    def __init__(self, width, height, order_manager, hud):
        self.width = width
        self.height = height
        self.order_manager = order_manager
        self.hud = hud
        self.font = pygame.font.Font(None, 42)
        self.small_font = pygame.font.Font(None, 24)
        self.message = "Ready to cook!"
        self.counter_image = None

        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
        counter_path = os.path.join(base_dir, "assets", "image", "ui", "meja_kasir.png")
        if os.path.exists(counter_path):
            counter = pygame.image.load(counter_path).convert_alpha()
            scale = min(900 / counter.get_width(), 300 / counter.get_height())
            new_size = (max(1, int(counter.get_width() * scale)), max(1, int(counter.get_height() * scale)))
            self.counter_image = pygame.transform.smoothscale(counter, new_size)

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return None

        if event.key == pygame.K_ESCAPE:
            return "exit"

        if event.key == pygame.K_SPACE:
            orders = self.order_manager.get_orders()
            if orders:
                order = orders[0]
                price = self.order_manager.complete_order(0)
                self.hud.add_money(price)
                self.message = f"{order.name} delivered! +${price}"
            else:
                self.message = "No active orders. Go back and wait for new ones."

        return None

    def draw(self, surface):
        surface.fill((30, 30, 35))

        title = self.font.render("Kitchen POV", True, (240, 240, 240))
        surface.blit(title, (30, 30))

        subtitle = self.small_font.render("Press SPACE to cook the next order, ESC to return.", True, (200, 200, 200))
        surface.blit(subtitle, (30, 82))

        orders = self.order_manager.get_orders()
        if orders:
            active = orders[0]
            order_text = self.font.render(f"Current order: {active.name}", True, (255, 220, 140))
            surface.blit(order_text, (30, 140))

            detail = self.small_font.render(f"Price: ${active.price}  |  Ready to serve with SPACE", True, (220, 220, 220))
            surface.blit(detail, (30, 190))
        else:
            no_order = self.font.render("No active order yet.", True, (200, 200, 200))
            surface.blit(no_order, (30, 140))

        message_surf = self.small_font.render(self.message, True, (180, 220, 180))
        surface.blit(message_surf, (30, self.height - 60))

        if self.counter_image is not None:
            counter_rect = self.counter_image.get_rect(midbottom=(self.width // 2, self.height - 20))
            surface.blit(self.counter_image, counter_rect)
        else:
            counter_rect = pygame.Rect(self.width // 2 - 420, self.height - 180, 840, 160)
            pygame.draw.rect(surface, (55, 55, 60), counter_rect, border_radius=18)
            pygame.draw.rect(surface, (110, 110, 120), counter_rect, 4, border_radius=18)
            counter_label = self.small_font.render("Kitchen counter", True, (210, 210, 210))
            surface.blit(counter_label, (counter_rect.x + 18, counter_rect.y + 18))
