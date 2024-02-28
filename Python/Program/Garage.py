# Saya Syifa Azzahra NIM 2207308 mengerjakan soal Latihan 4 dalam mata kuliah 
# Desain Pemrograman Berorientasi Objek untuk keberkahan-Nya maka saya tidak melakukan kecurangan seperti yang telah
# dispesifikasikan. Aamiin. 

class Garage:
# kelas yang digunakan untuk mengimplementasikan kelas Garage

    def __init__(self, luasGarasi="", daftarKendaraan=""):
        self.luasGarasi = luasGarasi
        self.daftarKendaraan = daftarKendaraan
    
    # mengeset dan mengembalikan atribut-atribut pada kelas Garage
    def setLuasGarasi(self, luasGarasi):
        self.luasGarasi = luasGarasi

    def getLuasGarasi(self):
        return self.luasGarasi
    
    def setDaftarKendaraan(self, daftarKendaraan):
        self.daftarKendaraan = daftarKendaraan

    def getDaftarKendaraan(self):
        return self.daftarKendaraan