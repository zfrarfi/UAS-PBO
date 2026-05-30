import pygame

class MainMenu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.bg_color = (245, 245, 245)
        self.panel_rect = pygame.Rect(0, 0, width // 3, height)
        self.title_font = pygame.font.Font(None, 80)
        self.sub_font = pygame.font.Font(None, 30)
        self.item_font = pygame.font.Font(None, 38)
        self.status_font = pygame.font.Font(None, 24)
        self.items = ["Start", "Load", "Preferences", "Help", "About", "Quit"]
        self.item_rects = []
        self.hover_index = None
        self.active = True
        self.status_text = "Click an option to continue"
        self.option_active = False
        self.option_title = ""
        self.option_rect = pygame.Rect(0, 0, 0, 0)
        self.close_rect = pygame.Rect(0, 0, 0, 0)
        self._create_item_rects()

    def set_status(self, text):
        self.status_text = text

    def show_option(self, action):
        self.option_active = True
        self.option_title = action
        self.status_text = f"{action} selected - coming soon"

    def _create_item_rects(self):
        base_y = 220
        item_width = self.panel_rect.width - 80
        for index in range(len(self.items)):
            rect = pygame.Rect(40, base_y + index * 70, item_width, 52)
            self.item_rects.append(rect)

    def draw(self, surface):
        pygame.draw.rect(surface, (230, 230, 230), (self.panel_rect.right, 0, 6, self.height))
        pygame.draw.rect(surface, self.bg_color, self.panel_rect)
        pygame.draw.rect(surface, (200, 200, 200), self.panel_rect, 2)

        title1 = self.title_font.render("Midnight", True, (25, 25, 25))
        title2 = self.title_font.render("Cafe", True, (25, 25, 25))
        surface.blit(title1, (40, 40))
        surface.blit(title2, (40, 120))

        subtitle = self.sub_font.render("A cozy cafe adventure", True, (80, 80, 80))
        surface.blit(subtitle, (40, 200))

        pygame.draw.line(surface, (210, 210, 210), (40, 235), (self.panel_rect.width - 40, 235), 2)

        for index, text in enumerate(self.items):
            rect = self.item_rects[index]
            if self.hover_index == index:
                pygame.draw.rect(surface, (220, 235, 255), rect, border_radius=12)
                pygame.draw.rect(surface, (145, 180, 235), rect, 2, border_radius=12)
            else:
                pygame.draw.rect(surface, (245, 245, 245), rect, border_radius=12)
            label = self.item_font.render(text, True, (25, 25, 25))
            surface.blit(label, (rect.x + 20, rect.y + (rect.height - label.get_height()) // 2))

        if self.status_text:
            status_label = self.status_font.render(self.status_text, True, (90, 90, 90))
            surface.blit(status_label, (40, self.height - 60))

        if self.option_active:
            self._draw_option_popup(surface)

    def _draw_option_popup(self, surface):
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 130))
        surface.blit(overlay, (0, 0))

        box_width = self.width // 2
        box_height = self.height // 3
        box_x = self.width // 2 - box_width // 2
        box_y = self.height // 2 - box_height // 2
        self.option_rect = pygame.Rect(box_x, box_y, box_width, box_height)

        pygame.draw.rect(surface, (245, 245, 245), self.option_rect, border_radius=18)
        pygame.draw.rect(surface, (170, 170, 170), self.option_rect, 2, border_radius=18)

        title = self.item_font.render(self.option_title, True, (25, 25, 25))
        surface.blit(title, (box_x + 32, box_y + 32))

        body = self.status_font.render("This feature is coming soon.", True, (70, 70, 70))
        surface.blit(body, (box_x + 32, box_y + 110))

        self.close_rect = pygame.Rect(box_x + box_width - 120, box_y + box_height - 60, 90, 40)
        pygame.draw.rect(surface, (225, 225, 225), self.close_rect, border_radius=12)
        pygame.draw.rect(surface, (180, 180, 180), self.close_rect, 1, border_radius=12)
        close_label = self.status_font.render("Close", True, (35, 35, 35))
        surface.blit(close_label, (self.close_rect.x + 22, self.close_rect.y + 11))

    def update_hover(self, mouse_pos):
        self.hover_index = None
        for index, rect in enumerate(self.item_rects):
            if rect.collidepoint(mouse_pos):
                self.hover_index = index
                break

    def handle_event(self, event):
        if self.option_active:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.close_rect.collidepoint(event.pos):
                    self.option_active = False
                    self.status_text = ""
            return None

        if event.type == pygame.MOUSEMOTION:
            self.update_hover(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.hover_index is not None:
                return self.items[self.hover_index]
        return None