from produk import Produk

class Tablet(Produk):
    def __init__(self, nama, harga, ukuran_layar):
        # Menggunakan super() untuk mewarisi nama dan harga
        super().__init__(nama, harga)
        self.ukuran_layar = ukuran_layar # Properti spesifik tablet

    def deskripsi(self):
        # Memanggil deskripsi induk dan menambah info layar
        return f"[Tablet] {super().deskripsi()} | Layar: {self.ukuran_layar} inch"