import pygame
import os


class Furniture:
    def __init__(self, nama, x, y, image_path, width, height):
        self.nama = nama
        self.x_position = x
        self.y_position = y
        self.level = 1

        # Load gambar dengan sistem yang kebal error
        self.image = self._load_image(image_path, width, height)

        # Kotak gaib (hitbox) collision untuk menahan pergerakan karakter
        self.rect = pygame.Rect(x, y, width, height)

    def _load_image(self, path, width, height):
        if os.path.exists(path):
            img = pygame.image.load(path).convert_alpha()
            return pygame.transform.scale(img, (width, height))
        else:
            print(f"Peringatan: '{path}' tidak ditemukan. Memakai kotak coklat untuk {self.nama}.")
            placeholder = pygame.Surface((width, height))
            placeholder.fill((139, 69, 19))  # Warna coklat
            return placeholder

    def upgrade_furniture(self, new_image_path, new_width, new_height):
        self.level += 1
        self.image = self._load_image(new_image_path, new_width, new_height)
        self.rect = pygame.Rect(self.x_position, self.y_position, new_width, new_height)

    def gambarFurniture(self, screen):
        screen.blit(self.image, (self.x_position, self.y_position))