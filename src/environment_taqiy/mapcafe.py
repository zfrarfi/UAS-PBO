import pygame
import os
from environment_taqiy.furniture import Furniture


class MapCafe:
    def __init__(self, x_position=0, y_position=0):
        self.x_position = x_position
        self.y_position = y_position

        self.base_map = None
        self.list_furniture = []
        self.static_collisions = []

        self._load_assets()
        self._setup_furniture()

    def _load_assets(self):
        # Memuat lantai utama
        path_lantai = "assets/image/map/lantai_luas.png"

        if os.path.exists(path_lantai):
            self.base_map = pygame.image.load(path_lantai).convert()

            self.base_map = pygame.transform.scale(
                self.base_map,
                (1280, 720)
            )
        else:
            print(f"Peringatan: {path_lantai} tidak ditemukan! Memakai lantai abu-abu.")
            self.base_map = pygame.Surface((1280, 720))
            self.base_map.fill((40, 40, 40))

    def _setup_furniture(self):
        # TEMBOK ATAS
        self.wall_top = pygame.Rect(960,0,330,300)

        # Simpan ke collision list
        self.static_collisions.append(self.wall_top)

        # Angka X, Y, Lebar, Tinggi di bawah ini bisa Paduka ganti-ganti nanti
        self.tembok_tengah = Furniture("tembok kiri atas 2", 995, 230, "assets/image/map/tembok.png", 320, 90)
        self.tembok_atas3 = Furniture("tembok kiri atas 2", 640, 0, "assets/image/map/tembok.png", 320, 90)
        self.tembok_atas2 = Furniture("tembok kiri atas 2", 320, 0, "assets/image/map/tembok.png", 320, 90)
        self.tembok_atas1 = Furniture("tembok kiri atas", 0, 0, "assets/image/map/tembok.png", 320, 90)

        #kiri
        self.sofa_kiri_depan_1 = Furniture("Sofa Kiri 1", 90, 100, "assets/image/map/sofa_depan.png", 135, 70)
        self.meja_kayu_1 = Furniture("Meja Kayu 1", 105, 173, "assets/image/map/meja_kayu.png", 106, 60)
        self.sofa_kiri_belakang_1 = Furniture("Sofa Kiri 1", 90, 227, "assets/image/map/sofa_belakang.png", 135, 70)

        #tengah kiri
        self.sofa_tengah_depan_1 = Furniture("Sofa tengah 1", 90, 100, "assets/image/map/sofa_depan.png", 135, 70)
        self.meja_kayu_tengah_1 = Furniture("Meja Kayu tengah 1", 105, 173, "assets/image/map/meja_kayu.png", 106, 60)
        self.sofa_tengah_belakang_1 = Furniture("Sofa tengah 1", 90, 227, "assets/image/map/sofa_belakang.png", 135, 70)


        # 3. MEJA KASIR
        self.meja_kasir = Furniture("Meja Kasir Utama", 296, 8, "assets/image/map/meja_kasir.png", 720, 307)

        # 4. REGISTRASI KE LIST (Jangan sampai terlewat)
        self.list_furniture = [
            self.tembok_tengah,
            self.tembok_atas3,
            self.tembok_atas2,
            self.tembok_atas1,

            self.sofa_kiri_depan_1,
            self.sofa_kiri_belakang_1,
            self.meja_kayu_1,

            self.sofa_tengah_depan_1,
            self.meja_kayu_tengah_1,
            self.sofa_tengah_belakang_1,

            self.meja_kasir
        ]

    def gambarMap(self, screen):
            screen.blit(
                self.base_map,
                (self.x_position, self.y_position)
            )

            # Gambar tembok coklat
            pygame.draw.rect(screen,(46, 24, 26),
                self.wall_top)

            for furn in self.list_furniture:
                furn.gambarFurniture(screen)

    def get_collisions(self):
        # Kumpulkan semua hitbox (tembok + perabotan)
        all_collisions = list(self.static_collisions)
        for furn in self.list_furniture:
            all_collisions.append(furn.rect)

        return all_collisions