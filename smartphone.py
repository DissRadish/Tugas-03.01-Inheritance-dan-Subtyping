from produk import Produk  # Import induknya

class Smartphone(Produk):
    def __init__(self, nama, harga, kamera_mp):
        super().__init__(nama, harga)
        self.kamera_mp = kamera_mp

    def deskripsi(self):
        return f"[Smartphone] {super().deskripsi()} | Kamera: {self.kamera_mp}MP"