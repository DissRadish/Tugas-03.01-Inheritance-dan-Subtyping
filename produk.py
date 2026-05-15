class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def deskripsi(self):
        return f"{self.nama} - Harga: Rp{self.harga:,}"