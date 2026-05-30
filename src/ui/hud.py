import pygame
import time

class Hud:
    """Simple HUD: shows elapsed time, money and active orders."""
    def __init__(self, barista=None, order_manager=None, start_money=0):
        self.barista = barista
        self.order_manager = order_manager
        self.money = start_money
        self.elapsed = 0.0
        self.font = pygame.font.Font(None, 24)
        self.small_font = pygame.font.Font(None, 20)

    def update(self, dt):
        self.elapsed += dt

    def add_money(self, amount):
        self.money += amount

    def draw(self, surface):
        w, h = surface.get_size()
        box_w = 220
        box_h = 72
        padding = 12
        x = w - box_w - padding
        y = padding

        # translucent background
        overlay = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 140))
        surface.blit(overlay, (x, y))

        # draw border
        pygame.draw.rect(surface, (200, 200, 200), (x, y, box_w, box_h), 1, border_radius=8)

        # time
        time_str = time.strftime('%M:%S', time.gmtime(int(self.elapsed)))
        t_surf = self.font.render(f"Time: {time_str}", True, (255, 255, 255))
        surface.blit(t_surf, (x + 12, y + 10))

        # money
        m_surf = self.font.render(f"Money: ${self.money}", True, (255, 255, 255))
        surface.blit(m_surf, (x + 12, y + 36))

        # optional: player pos
        if self.barista is not None and hasattr(self.barista, 'x_position'):
            pos_text = f"Pos: {int(self.barista.x_position)},{int(self.barista.y_position)}"
            p_surf = self.small_font.render(pos_text, True, (200, 200, 200))
            surface.blit(p_surf, (x + box_w - 12 - p_surf.get_width(), y + box_h - 18))

        # draw active orders (below the HUD box)
        if self.order_manager is not None:
            orders = self.order_manager.get_orders()
            ox = x
            oy = y + box_h + 12
            max_show = 5
            for i, o in enumerate(orders[:max_show]):
                line = f"{i+1}. {o.name} - ${o.price}"
                o_surf = self.small_font.render(line, True, (240, 240, 240))
                # draw darker translucent strip
                strip = pygame.Surface((box_w, 26), pygame.SRCALPHA)
                strip.fill((0, 0, 0, 120))
                surface.blit(strip, (ox, oy + i*30))
                surface.blit(o_surf, (ox + 8, oy + i*30 + 4))
