# Import semua kelas yang dibutuhkan
from laptop import Laptop
from smartphone import Smartphone

def cetak_label_inventaris(item):
    """Contoh Subtyping: menerima objek apa pun yang merupakan turunan Produk"""
    print(f"Mencetak Label: {item.deskripsi()}")

if __name__ == "__main__":
    laptop_pro = Laptop("Asus ROG", 18000000, 16)
    phone_pro = Smartphone("Samsung S24", 14000000, 50)

    print("=== SISTEM INVENTARIS TERPISAH ===\n")
    cetak_label_inventaris(laptop_pro)
    cetak_label_inventaris(phone_pro)