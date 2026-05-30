import pygame
import os


class Customer:
    def __init__(self, x_position, y_position):  # (parameter biarkan seperti aslinya)

        # 1. Lacak posisi file customer.py ini
        current_dir = os.path.dirname(__file__)

        # 2. Susun path otomatis (Naik 2 folder, lalu masuk ke assets/image/character)
        image_path = os.path.join(current_dir, "..", "..", "assets", "image", "character", "cust_front_frame1.png")

        # 3. Load gambar
        try:
            self.image = pygame.image.load(image_path).convert_alpha()
        except FileNotFoundError:
            # Jika gambar masih tidak ketemu, jangan biarkan gamenya crash!
            # Tampilkan kotak placeholder warna merah sementara
            print(f"Peringatan: Gambar tidak ditemukan di {image_path}")
            self.image = pygame.Surface((64, 64))
            self.image.fill((255, 0, 0))