from produk import Produk  # Import induknya

class Laptop(Produk):
    def __init__(self, nama, harga, ram):
        super().__init__(nama, harga)
        self.ram = ram

    def deskripsi(self):
        return f"[Laptop] {super().deskripsi()} | RAM: {self.ram}GB"