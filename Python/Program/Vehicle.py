# Saya Syifa Azzahra NIM 2207308 mengerjakan soal Latihan 4 dalam mata kuliah 
# Desain Pemrograman Berorientasi Objek untuk keberkahan-Nya maka saya tidak melakukan kecurangan seperti yang telah
# dispesifikasikan. Aamiin. 

class Vehicle:
# kelas yang digunakan untuk mengimplementasikan kelas Vehicle

    def __init__(self, platNomor="", merk="", tahunProduksi="", warna=""):
        self.platNomor = platNomor
        self.merk = merk
        self.tahunProduksi = tahunProduksi
        self.warna = warna

    # mengeset dan mengembalikan atribut-atribut pada kelas Vehicle
    def setPlatNomor(self, platNomor):
        self.platNomor = platNomor

    def getPlatNomor(self):
        return self.platNomor
    
    def setMerk(self, merk):
        self.merk = merk

    def getMerk(self):
        return self.merk
    
    def setTahunProduksi(self, tahunProduksi):
        self.tahunProduksi = tahunProduksi

    def getTahunProduksi(self):
        return self.tahunProduksi
    
    def setWarna(self, warna):
        self.warna = warna

    def getWarna(self):
        return self.warna