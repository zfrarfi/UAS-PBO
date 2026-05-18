from abc import ABC        

class Menu(ABC):
    def __init__(self, nama, harga, bahan):
        self.nama = nama
        self.harga = harga
        self.bahan = bahan
        
class Minuman(Menu):
    def __init__(self, nama, harga, bahan):
        super().__init__(nama, harga, bahan)
        
class Makanan(Menu):
    def __init__(self, nama, harga, bahan):
        super().__init__(nama, harga, bahan)