from laptop import Laptop
from smartphone import Smartphone
from tablet import Tablet  # Import kelas baru

def cetak_label_inventaris(item):
    """
    Inilah kekuatan SUBTYPING. 
    Meskipun kita tambah kelas baru (Tablet), fungsi ini 
    TIDAK PERLU diubah sama sekali karena Tablet adalah subtype dari Produk.
    """
    print(f"Mencetak Label: {item.deskripsi()}")

if __name__ == "__main__":
    # Inisialisasi berbagai macam objek
    laptop_pro = Laptop("Asus ROG", 18000000, 16)
    phone_pro = Smartphone("Samsung S24", 14000000, 50)
    tablet_pro = Tablet("iPad Air", 10500000, 10.9) # Objek baru

    print("=== SISTEM INVENTARIS TOKO (Update) ===\n")
    
    # Semua objek ini diperlakukan sebagai 'Produk' (Subtyping)
    cetak_label_inventaris(laptop_pro)
    cetak_label_inventaris(phone_pro)
    cetak_label_inventaris(tablet_pro)
