class Kuliner:
    def __init__(self, nama, harga):
        self.__nama = nama
        self.__harga = harga

    def getNama(self):
        return self.__nama

    def getHarga(self):
        return self.__harga

    def tampilkanInfo(self):
        print(f"{self.__nama} - Rp{self.__harga}")


class Makanan(Kuliner):
    def __init__(self, nama, harga, bahan):
        super().__init__(nama, harga)
        self.__bahan = bahan

    def tampilkanInfo(self):
        super().tampilkanInfo()
        print(f"Bahan: {self.__bahan}")


class Minuman(Kuliner):
    def __init__(self, nama, harga, ukuran):
        super().__init__(nama, harga)
        self.__ukuran = ukuran

    def tampilkanInfo(self):
        super().tampilkanInfo()
        print(f"Ukuran: {self.__ukuran}")


class MinumanPanas(Minuman):
    def __init__(self, nama, harga, ukuran, mengandungKafein):
        super().__init__(nama, harga, ukuran)
        self.__mengandungKafein = mengandungKafein

    def Kafein(self):
        return self.__mengandungKafein

    def tampilkanInfo(self):
        super().tampilkanInfo()
        print(f"Kandungan kafein: {self.Kafein()}")


print("========================")
menu = [
    Makanan("Nasi Goreng", 20000, "Nasi, Bumbu, Sayur"),
    Minuman("Es Teh", 5000, "Large"),
    MinumanPanas("Kopi Hitam", 8000, "Medium", True)
]



print("Menu Makanan:")
for i, item in enumerate(menu, start=1):
    print(f"{i}. {item.getNama()} - Rp{item.getHarga()}")

while True:    
        pilihan = int(input("\nPilih menu (1-3) atau ketik '0' untuk selesai: "))
        if pilihan == 0:
            print("Terima kasih atas pesanan Anda. Selamat menikmati!")
            break
        elif 1 <= pilihan <= len(menu):
            pesanan = menu[pilihan - 1]
            pesanan.tampilkanInfo()
            print("Pesanan diterima. Mohon tunggu sebentar.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")
    