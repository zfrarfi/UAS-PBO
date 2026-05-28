from abc import ABC        

class Menu(ABC):
    def __init__(self, nama, harga, bahan):
        self.nama = nama
        self.harga = harga
        self.bahan = bahan
        

        
