from abc import ABC, abstractmethod

class Menu(ABC):
    def __init__(self, nama, harga, bahan):
        self.nama = nama
        self.harga = harga
        self.bahan = bahan
        

        
