import pygame

class DialogueManager:
    def __init__(self):
        self.dialogues = []
        self.current_index = 0
        self.is_active = False
        self.order = None

    def start(self, dialogues):
        self.dialogues = dialogues
        self.current_index = 0
        self.is_active = True

    def next(self):
        self.current_index += 1
        if self.current_index >= len(self.dialogues):
            self.is_active = False

    def get_current(self):
        if self.is_active:
            return self.dialogues[self.current_index]
        return None

    def save_order(self, menu_item):
        self.order = menu_item
        
    def draw(self, screen):
        if not self.is_active:
            return
    
        current = self.get_current()
        if current is None:
            return

    # Kotak dialog
        pygame.draw.rect(screen, (30, 30, 30), (50, 500, 1180, 180), border_radius=12)
        pygame.draw.rect(screen, (255, 255, 255), (50, 500, 1180, 180), 2, border_radius=12)

        font_name = pygame.font.Font(None, 32)
        font_text = pygame.font.Font(None, 28)

    # Nama speaker
        speaker_surf = font_name.render(current["speaker"], True, (255, 220, 100))
        screen.blit(speaker_surf, (80, 520))

    # Teks dialog
        text_surf = font_text.render(current["text"], True, (255, 255, 255))
        screen.blit(text_surf, (80, 560))

    # Petunjuk lanjut
        hint_surf = font_text.render("Tekan SPACE untuk lanjut", True, (180, 180, 180))
        screen.blit(hint_surf, (980, 650))