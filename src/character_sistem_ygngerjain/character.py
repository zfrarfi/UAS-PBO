import time
import pygame
class Character:
    
    SPEED = 3
    
    def __init__(self, x_position, y_position, name, bubble_chat):
        self.x_position = x_position
        self.y_position = y_position
        self.name = name
        self.bubble_chat = bubble_chat  
        
        self.bubble_timer = 0.0
        self.bubble_text = ""
        self.bubble_surface = None
        
    def load_bubble_asset(cls, path):
        cls.BUBBLE_ASSET = pygame.image.load(path).convert_alpha()
    
    def tampilkan_bubble_chat(self, text):
        self.bubble_chat   = text
        self._bubble_text  = text
        self._bubble_timer = time.time()
        print(f"[BUBBLE] {self.name}: {text}")
        return text
    
    def gerak(self):
        raise NotImplementedError("Subclass harus override gerak()")
    
    def bubble_visible(self, duration=3.0):
        if not self._bubble_text:
            return False
        return (time.time() - self._bubble_timer) < duration
    
    def get_rect(self):
        return pygame.Rect(self.x_position, self.y_position, 32, 48)
    
    def _draw_bubble(self, surface, text):

        font  = pygame.font.SysFont("Arial", 13)
        label = font.render(text, True, (20, 20, 20))
        pad   = 8
        bw    = label.get_width()  + pad * 2
        bh    = label.get_height() + pad * 2
        bx    = self.x_position - bw // 4
        by    = self.y_position - bh - 10
 
        if self.BUBBLE_ASSET:
            bubble_img = pygame.transform.scale(self.BUBBLE_ASSET, (bw, bh))
            surface.blit(bubble_img, (bx, by))
        else:
            pygame.draw.rect(surface, (255, 255, 240),
                            (bx, by, bw, bh), border_radius=6)
            pygame.draw.rect(surface, (100, 100, 80),
                            (bx, by, bw, bh), 1, border_radius=6)
            pygame.draw.polygon(surface, (255, 255, 240), [
                (bx + bw // 2 - 5, by + bh),
                (bx + bw // 2 + 5, by + bh),
                (bx + bw // 2,     by + bh + 7),
            ])
 
        # Teks selalu di-render di atas (asset maupun fallback)
        surface.blit(label, (bx + pad, by + pad))

