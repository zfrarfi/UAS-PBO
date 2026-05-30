import pygame
import os
from environment.furniture import Furniture


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
        self.wall_top2 = pygame.Rect(1050,475,330,300)
        # Simpan ke collision list
        self.static_collisions.append(self.wall_top)
        self.static_collisions.append(self.wall_top2)

        # Kasir Kiri
        self.kasir_left = pygame.Rect(300, 0, 115, 190)

        # Kasir Bawah
        self.kasir_bottom = pygame.Rect(395,215,448,92)

        #kulkas minuman
        self.kulkas_minuman = pygame.Rect(955,50,50,150)

        # Kulkas
        self.kulkas_collision = pygame.Rect(940,195,60,118)

        #sudut kiri bawah
        self.sudut1 = pygame.Rect(320, 170, 95, 65)
        self.sudut2 = pygame.Rect(350, 190, 70, 90)

        self.static_collisions.extend([
            self.sudut1,
            self.sudut2,
            self.kulkas_minuman,
            self.kasir_left,
            self.kasir_bottom,
            self.kulkas_collision
        ])

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
        self.sofa_tengah_depan_1 = Furniture("Sofa tengah 1", 90, 400, "assets/image/map/sofa_depan.png", 135, 70)
        self.meja_kayu_tengah_1 = Furniture("Meja Kayu tengah 1", 105, 473, "assets/image/map/meja_kayu.png", 106, 60)
        self.sofa_tengah_belakang_1 = Furniture("Sofa tengah 1", 90, 527, "assets/image/map/sofa_belakang.png", 135, 70)

        #tengah kiri 2
        self.sofa_tengah_depan_2 = Furniture("Sofa tengah 2", 290, 400, "assets/image/map/sofa_depan.png", 135, 70)
        self.meja_kayu_tengah_2 = Furniture("Meja Kayu tengah 2", 305, 473, "assets/image/map/meja_kayu.png", 106, 60)
        self.sofa_tengah_belakang_2 = Furniture("Sofa tengah 2", 290, 527, "assets/image/map/sofa_belakang.png", 135, 70)

        #tengah kiri 3
        self.sofa_tengah_depan_3 = Furniture("Sofa tengah 2", 490, 400, "assets/image/map/sofa_depan.png", 135, 70)
        self.meja_kayu_tengah_3 = Furniture("Meja Kayu tengah 2", 505, 473, "assets/image/map/meja_kayu.png", 106, 60)
        self.sofa_tengah_belakang_3 = Furniture("Sofa tengah 2", 490, 527, "assets/image/map/sofa_belakang.png", 135, 70)

        # tengah kiri 4
        self.sofa_tengah_depan_4 = Furniture("Sofa tengah 2", 690, 400, "assets/image/map/sofa_depan.png", 135, 70)
        self.meja_kayu_tengah_4 = Furniture("Meja Kayu tengah 2", 705, 473, "assets/image/map/meja_kayu.png", 106, 60)
        self.sofa_tengah_belakang_4 = Furniture("Sofa tengah 2", 690, 527, "assets/image/map/sofa_belakang.png", 135,
                                                70)
        #kasir
        self.meja_kasir = Furniture("Meja Kasir Utama", 296, 8, "assets/image/map/meja_kasir.png", 720, 307)

        #kursi bawah 1
        self.kursi_bawah1_1 = Furniture("kursi bawah 2/1", 102, 635, "assets/image/map/kursi_bawah.png", 33, 43)
        self.kursi_bawah1_2 = Furniture("kursi bawah 2/2", 150, 635, "assets/image/map/kursi_bawah.png", 33, 43)

        #kursi bawah 2
        self.kursi_bawah2_1 = Furniture("kursi bawah 2/1", 208, 635, "assets/image/map/kursi_bawah.png", 33, 43)
        self.kursi_bawah2_2 = Furniture("kursi bawah 2/2", 254, 635, "assets/image/map/kursi_bawah.png", 33, 43)

        #kursi bawah 3
        self.kursi_bawah3_1 = Furniture("kursi bawah 2/1", 316, 635, "assets/image/map/kursi_bawah.png", 33, 43)
        self.kursi_bawah3_2 = Furniture("kursi bawah 2/2", 362, 635, "assets/image/map/kursi_bawah.png", 33, 43)

        #kursi bawah 4
        self.kursi_bawah4_1 = Furniture("kursi bawah 2/1", 424, 635, "assets/image/map/kursi_bawah.png", 33, 43)
        self.kursi_bawah4_2 = Furniture("kursi bawah 2/2", 470, 635, "assets/image/map/kursi_bawah.png", 33, 43)

        #kursi bawah 5
        self.kursi_bawah5_1 = Furniture("kursi bawah 2/1", 531, 635, "assets/image/map/kursi_bawah.png", 33, 43)
        self.kursi_bawah5_2 = Furniture("kursi bawah 2/2", 577, 635, "assets/image/map/kursi_bawah.png", 33, 43)

        #kursi bawah 6
        self.kursi_bawah6_1 = Furniture("kursi bawah 2/1", 638, 635, "assets/image/map/kursi_bawah.png", 33, 43)
        self.kursi_bawah6_2 = Furniture("kursi bawah 2/2", 684, 635, "assets/image/map/kursi_bawah.png", 33, 43)

        #kursi bawah 7
        self.kursi_bawah7_1 = Furniture("kursi bawah 2/1", 745, 635, "assets/image/map/kursi_bawah.png", 33, 43)
        self.kursi_bawah7_2 = Furniture("kursi bawah 2/2", 791, 635, "assets/image/map/kursi_bawah.png", 33, 43)

        #kursi bawah 8
        self.kursi_bawah8_1 = Furniture("kursi bawah 2/1", 852, 635, "assets/image/map/kursi_bawah.png", 33, 43)
        self.kursi_bawah8_2 = Furniture("kursi bawah 2/2", 898, 635, "assets/image/map/kursi_bawah.png", 33, 43)

        #kursi bawah 9
        self.kursi_bawah9_1 = Furniture("kursi bawah 2/1", 959, 635, "assets/image/map/kursi_bawah.png", 33, 43)
        self.kursi_bawah9_2 = Furniture("kursi bawah 2/2", 1005, 635, "assets/image/map/kursi_bawah.png", 33, 43)

        #bawah
        self.meja_panjang = Furniture("Meja Panjang", 90, 672, "assets/image/map/meja_panjang.png", 960, 67)


        # 4. REGISTRASI KE LIST (Jangan sampai terlewat)
        self.list_furniture = [
            self.tembok_tengah,
            self.tembok_atas3,
            self.tembok_atas2,
            self.tembok_atas1,

            #kiri
            self.sofa_kiri_depan_1,
            self.sofa_kiri_belakang_1,
            self.meja_kayu_1,
            #tengah 1

            self.sofa_tengah_depan_1,
            self.meja_kayu_tengah_1,
            self.sofa_tengah_belakang_1,

            #tengah 2
            self.sofa_tengah_depan_2,
            self.meja_kayu_tengah_2,
            self.sofa_tengah_belakang_2,

            # tengah 3
            self.sofa_tengah_depan_3,
            self.meja_kayu_tengah_3,
            self.sofa_tengah_belakang_3,

            # tengah 4
            self.sofa_tengah_depan_4,
            self.meja_kayu_tengah_4,
            self.sofa_tengah_belakang_4,

            #kursi kecil
            self.kursi_bawah1_1,
            self.kursi_bawah1_2,
            self.kursi_bawah2_1,
            self.kursi_bawah2_2,
            self.kursi_bawah3_1,
            self.kursi_bawah3_2,
            self.kursi_bawah4_1,
            self.kursi_bawah4_2,
            self.kursi_bawah5_1,
            self.kursi_bawah5_2,
            self.kursi_bawah6_1,
            self.kursi_bawah6_2,
            self.kursi_bawah7_1,
            self.kursi_bawah7_2,
            self.kursi_bawah8_1,
            self.kursi_bawah8_2,
            self.kursi_bawah9_1,
            self.kursi_bawah9_2,

            # Panjang bawah
            self.meja_panjang,

            #kasir
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

            pygame.draw.rect(screen,(46, 24, 26),
                self.wall_top2)

            for furn in self.list_furniture:
                furn.gambarFurniture(screen)

            for rect in self.static_collisions:
                pygame.draw.rect(
                    screen,
                    (0, 255, 0),
                    rect,
                    2
                )

    def get_collisions(self):
        all_collisions = list(self.static_collisions)

        for furn in self.list_furniture:

            if furn == self.meja_kasir:
                continue

            all_collisions.append(furn.rect)

        return all_collisions
