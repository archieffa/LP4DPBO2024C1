# Saya Syifa Azzahra NIM 2207308 mengerjakan soal Latihan 4 dalam mata kuliah 
# Desain Pemrograman Berorientasi Objek untuk keberkahan-Nya maka saya tidak melakukan kecurangan seperti yang telah
# dispesifikasikan. Aamiin. 

from Vehicle import Vehicle

class Car(Vehicle):
# kelas yang digunakan untuk mengimplementasikan kelas Car
    
    def __init__(self, platNomor, merk, tahunProduksi, warna, jenisMobil, jumlahKursi, jumlahPintu, namaVehicleStorage, lokasi):
        super().__init__(platNomor, merk, tahunProduksi, warna)
        self.jenisMobil = jenisMobil
        self.jumlahKursi = jumlahKursi
        self.jumlahPintu = jumlahPintu
        self.namaVehicleStorage = namaVehicleStorage
        self.lokasi = lokasi

    # mengeset dan mengembalikan atribut-atribut pada kelas Car
    def setJenisMobil(self, jenisMobil):
        self.jenisMobil = jenisMobil
    
    def getJenisMobil(self):
        return self.jenisMobil

    def setJumlahKursi(self, jumlahKursi):
        self.jumlahKursi = jumlahKursi

    def getJumlahKursi(self):
        return self.jumlahKursi
    
    def setJumlahPintu(self, jumlahPintu):
        self.jumlahPintu = jumlahPintu

    def getJumlahPintu(self):
        return self.jumlahPintu

    def setNamaVehicleStorage(self, namaVehicleStorage):
        self.namaVehicleStorage = namaVehicleStorage

    def getNamaVehicleStorage(self):
        return self.namaVehicleStorage
    
    def setLokasi(self, lokasi):
        self.lokasi = lokasi

    def getLokasi(self):
        return self.lokasi