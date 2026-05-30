import os
import pygame
from kitchen.recipes import get_recipe

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
        self.order_rects = []
        self.ingredient_rects = []
        self.selected_order_index = None
        self.selected_order_recipe = None
        self.selected_ingredients = []

        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
        counter_path = os.path.join(base_dir, "assets", "image", "ui", "meja_kasir.png")
        if os.path.exists(counter_path):
            counter = pygame.image.load(counter_path).convert_alpha()
            scale = min(900 / counter.get_width(), 300 / counter.get_height())
            new_size = (max(1, int(counter.get_width() * scale)), max(1, int(counter.get_height() * scale)))
            self.counter_image = pygame.transform.smoothscale(counter, new_size)

    def select_order(self, index):
        orders = self.order_manager.get_orders()
        if 0 <= index < len(orders):
            self.selected_order_index = index
            self.selected_order_recipe = get_recipe(orders[index].name)
            self.selected_ingredients = []
            self.message = f"Selected {orders[index].name}. Tap ingredients to choose the right ones."
        else:
            self.selected_order_index = None
            self.selected_order_recipe = None
            self.selected_ingredients = []
            self.message = "No order selected."

    def toggle_ingredient(self, ingredient):
        if ingredient in self.selected_ingredients:
            self.selected_ingredients.remove(ingredient)
            self.message = f"{ingredient} removed from plate."
        else:
            self.selected_ingredients.append(ingredient)
            self.message = f"{ingredient} added to plate."

    def selection_is_correct(self):
        if self.selected_order_recipe is None:
            return False
        needed = list(self.selected_order_recipe.ingredients)
        chosen = list(self.selected_ingredients)
        return sorted(needed) == sorted(chosen)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "exit"
            if event.key == pygame.K_SPACE:
                if self.selected_order_index is None:
                    self.message = "Choose an order first."
                elif not self.selected_ingredients:
                    self.message = "Pick ingredients for the order first."
                elif not self.selection_is_correct():
                    self.message = "Wrong ingredients! Choose the correct ones."
                else:
                    price = self.order_manager.complete_order(self.selected_order_index)
                    if price > 0:
                        self.hud.add_money(price)
                        self.message = f"{self.selected_order_recipe.name if self.selected_order_recipe else 'Order'} delivered! +${price}"
                        self.selected_order_index = None
                        self.selected_order_recipe = None
                        self.selected_ingredients = []
                    else:
                        self.message = "Unable to deliver order. Try selecting again."
            return None

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for index, rect in enumerate(self.order_rects):
                if rect.collidepoint(event.pos):
                    self.select_order(index)
                    return None

            for idx, rect in enumerate(self.ingredient_rects):
                if rect.collidepoint(event.pos) and self.selected_order_recipe is not None:
                    ingredient = self.selected_order_recipe.ingredients[idx]
                    self.toggle_ingredient(ingredient)
                    return None

        return None

    def draw(self, surface):
        surface.fill((30, 30, 35))

        title = self.font.render("Kitchen POV", True, (240, 240, 240))
        surface.blit(title, (30, 30))

        subtitle = self.small_font.render("Click an order, pick the correct ingredients, then press SPACE to deliver. ESC to return.", True, (200, 200, 200))
        surface.blit(subtitle, (30, 82))

        orders = self.order_manager.get_orders()
        order_panel_x = 30
        order_panel_y = 140
        panel_width = 360
        self.order_rects = []

        if orders:
            header = self.font.render("Incoming orders:", True, (235, 205, 150))
            surface.blit(header, (order_panel_x, order_panel_y))
            for idx, order in enumerate(orders):
                rect = pygame.Rect(order_panel_x, order_panel_y + 70 + idx * 62, panel_width, 52)
                self.order_rects.append(rect)
                is_selected = idx == self.selected_order_index
                bg_color = (70, 70, 90) if is_selected else (45, 45, 55)
                border_color = (180, 180, 240) if is_selected else (90, 90, 110)
                pygame.draw.rect(surface, bg_color, rect, border_radius=12)
                pygame.draw.rect(surface, border_color, rect, 2, border_radius=12)
                order_label = self.small_font.render(f"{idx + 1}. {order.name}  -  ${order.price}", True, (240, 240, 240))
                surface.blit(order_label, (rect.x + 14, rect.y + 14))
        else:
            no_order = self.font.render("No active orders yet.", True, (200, 200, 200))
            surface.blit(no_order, (order_panel_x, order_panel_y))

        detail_panel_x = order_panel_x + panel_width + 40
        detail_panel_y = order_panel_y
        if self.selected_order_recipe is not None:
            recipe = self.selected_order_recipe
            current_label = self.font.render(f"Order: {recipe.name}", True, (255, 220, 140))
            surface.blit(current_label, (detail_panel_x, detail_panel_y))

            ingredient_label = self.small_font.render("Choose ingredients:", True, (220, 220, 220))
            surface.blit(ingredient_label, (detail_panel_x, detail_panel_y + 60))

            self.ingredient_rects = []
            for idx, ingredient in enumerate(recipe.ingredients):
                rect = pygame.Rect(detail_panel_x, detail_panel_y + 100 + idx * 56, 300, 46)
                self.ingredient_rects.append(rect)
                selected = ingredient in self.selected_ingredients
                fill_color = (85, 125, 80) if selected else (55, 55, 70)
                border_color = (170, 210, 170) if selected else (110, 110, 130)
                pygame.draw.rect(surface, fill_color, rect, border_radius=12)
                pygame.draw.rect(surface, border_color, rect, 2, border_radius=12)
                ingredient_text = self.small_font.render(ingredient, True, (245, 245, 245))
                surface.blit(ingredient_text, (rect.x + 16, rect.y + 12))

            selected_text = self.small_font.render(
                f"Selected: {', '.join(self.selected_ingredients) if self.selected_ingredients else 'none'}",
                True,
                (200, 220, 200),
            )
            surface.blit(selected_text, (detail_panel_x, detail_panel_y + 100 + len(recipe.ingredients) * 56 + 16))
        elif orders:
            hint = self.small_font.render("Select one order to see its ingredients.", True, (180, 180, 200))
            surface.blit(hint, (detail_panel_x, detail_panel_y))
        else:
            self.ingredient_rects = []

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
