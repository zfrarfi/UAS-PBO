import pygame
from character import Character
from enums import BaristaState, CustomerState



class Barista(Character):
    CASHIER_ZONE = pygame.Rect(350, 80, 80, 80)
    SERVE_RANGE  = 60
    
    ASSET_IDLE = None
    ASSET_WALK = None
    
    
    def __init__(self, x_position, y_position, name, bubble_chat, money, saldo):
        super().__init__(x_position, y_position, name, bubble_chat)

        self.money = 0
        self.saldo = 500000
        
        self.state =BaristaState.IDLE
        self.current_order = ""
        self.serving_customer= None
        
        self.sprite_idle = None
        self.sprite_walk = None
        
    def load_assets(cls, path_idle, path_walk):
        cls.ASSET_IDLE = pygame.image.load(path_idle).convert_alpha()
        cls.ASSET_WALK = pygame.image.load(path_walk).convert_alpha()
        
    def draw(self, surface, sprite=None):

        if self.ASSET_IDLE and self.ASSET_WALK:
            aktif = self.ASSET_WALK if self.state == BaristaState.WALKING \
                    else self.ASSET_IDLE
            super().draw(surface, sprite=aktif)
        else:
            super().draw(surface)   

    def tampilkan_bubble_chat(self, text):
        return super().tampilkan_bubble_chat(text)

    def pesanan(self):
        return self.current_order

    def gerakkan(self):
        """
        Kontrol gerakan WASD.
        Return True jika bergerak, False jika tidak / sedang servis.
        """
        if self.state in (BaristaState.SERVING, BaristaState.MAKING):
            return False

        keys  = pygame.key.get_pressed()
        moved = False
        speed = self.SPEED

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.y_position -= speed
            moved = True
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.y_position += speed
            moved = True
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x_position -= speed
            moved = True
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x_position += speed
            moved = True

        self.x_position = max(0, min(self.x_position, 768))
        self.y_position = max(0, min(self.y_position, 552))

        self.state = BaristaState.WALKING if moved else BaristaState.IDLE
        return moved

    def getMoney(self):
        return float(self.money)

    def gerak(self):
        self.gerakkan()

    # ── Logika servis ────────────────────────────────────────────────

    def cek_area_kasir(self):
        return self.get_rect().colliderect(self.CASHIER_ZONE)

    def mulai_servis(self, customer):
        self.state             = BaristaState.SERVING
        self._serving_customer = customer
        customer.state         = CustomerState.ORDERING
        sapa = f"Halo {customer.name}! Selamat datang di Cozy Midnight Cafe~"
        self.tampilkan_bubble_chat(sapa)
        print(f"[SERVIS] {self.name} melayani {customer.name}")
        print("[POV] Kamera beralih ke meja kasir")

    def terima_pesanan(self, customer):
        self.tampilkan_bubble_chat("Mau pesan apa hari ini?")
        order = customer.beri_pesanan()
        self.current_order = order
        print(f"[PESANAN] {customer.name} memesan: {order}")
        return order

    def buat_pesanan(self):
        self.state = BaristaState.MAKING
        print(f"[MAKING] Membuat: {self.current_order}")
        print("[POV] Kamera beralih ke area pembuatan")
        return True

    def antar_pesanan(self, customer):
        if self.state != BaristaState.MAKING:
            print("[ERROR] Pesanan belum dibuat!")
            return
        harga       = customer.bayar()
        self.money += harga
        self.saldo += harga
        self.tampilkan_bubble_chat("Ini pesanannya! Terima kasih ya")
        print(f"[BAYAR] +Rp{harga:,} | Saldo: Rp{self.saldo:,}")
        customer.state         = CustomerState.LEAVING
        self.state             = BaristaState.IDLE
        self._serving_customer = None
        self.current_order     = ""
        print("[POV] Kamera kembali ke cafe")
