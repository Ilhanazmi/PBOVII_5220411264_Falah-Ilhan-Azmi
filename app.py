import mysql.connector

class DatabaseKuliner:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='5220411264'
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def fetch_data(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

class MenuKuliner:
    def __init__(self):
        self.db_manager = DatabaseKuliner()

    def display_menu(self):
        print('Silahkan pilih opsi dibawah:')
        print('1. Tampilkan Menu Kuliner')
        print('2. Tambah Menu Kuliner')
        print('3. Ubah Menu Kuliner')
        print('4. Hapus Menu Kuliner')
        print('5. Keluar')

    def tampilkan_menu_kuliner(self):
        query = 'SELECT * FROM menu_kuliner'
        results = self.db_manager.fetch_data(query)
        for row in results:
            print(row)

    def tambah_menu_kuliner(self):
        nama_menu = input('Masukkan nama menu: ')
        harga = input('Masukkan harga: ')
        deskripsi = input('Masukkan deskripsi: ')

        query = f"INSERT INTO menu_kuliner (nama_menu, harga, deskripsi) VALUES ('{nama_menu}', {harga}, '{deskripsi}')"
        
        self.db_manager.execute_query(query)
        print('Menu kuliner berhasil ditambahkan.')

    def ubah_menu_kuliner(self):
        self.tampilkan_menu_kuliner()
        id_menu = input('Masukkan ID menu yang ingin diubah: ')
        harga_baru = input('Masukkan harga baru: ')
        
        query = f"UPDATE menu_kuliner SET harga = {harga_baru} WHERE id_menu = {id_menu}"
        
        self.db_manager.execute_query(query)
        print('Menu kuliner berhasil diubah.')

    def hapus_menu(self):
        self.tampilkan_menu_kuliner()
        id_menu = input('Masukkan ID menu yang ingin dihapus: ')
        
        query = f"DELETE FROM menu_kuliner WHERE id_menu = {id_menu}"
        
        self.db_manager.execute_query(query)
        print('Menu kuliner berhasil dihapus.')

    def start_program(self):
        while True:
            self.display_menu()
            choice = input('Pilih menu (1-5): ')

            if choice == '1':
                self.tampilkan_menu_kuliner()
            elif choice == '2':
                self.tambah_menu_kuliner()
            elif choice == '3':
                self.ubah_menu_kuliner()
            elif choice == '4':
                self.hapus_menu()
            elif choice == '5':
                self.exit_program()
            else:
                print('Pilihan tidak valid. Silakan coba lagi.')

    def exit_program(self):
        self.db_manager.close_connection()
        print('Program selesai.')
        exit()

if __name__ == "__main__":
    menu_program = MenuKuliner()
    menu_program.start_program()
