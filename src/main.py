import pygame
import sys
from environment_taqiy.mapcafe import MapCafe


def main():
    pygame.init()

    # Ukuran jendela game (Sesuaikan jika resolusi gambar lantai berbeda)
    WIDTH, HEIGHT = 1280, 720
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Midnight Cafe - Environment Area (King Fauzan Paduka)")

    clock = pygame.time.Clock()

    # HANYA meload sistem Map dan Furniture
    map_cafe = MapCafe(0, 0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Bersihkan layar tiap frame
        screen.fill((0, 0, 0))

        # Render semua tata letak cafe
        map_cafe.gambarMap(screen)

        # ========================================================
        # MODE DEBUG: Menampilkan garis merah untuk mengecek tabrakan
        # Sangat berguna untuk kalibrasi koordinat X dan Y perabotan
        # ========================================================
        for hitbox in map_cafe.get_collisions():
            pygame.draw.rect(screen, (255, 0, 0), hitbox, 2)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()