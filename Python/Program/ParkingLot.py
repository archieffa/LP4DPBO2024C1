# Saya Syifa Azzahra NIM 2207308 mengerjakan soal Latihan 4 dalam mata kuliah 
# Desain Pemrograman Berorientasi Objek untuk keberkahan-Nya maka saya tidak melakukan kecurangan seperti yang telah
# dispesifikasikan. Aamiin. 

class ParkingLot:
# kelas yang digunakan untuk mengimplementasikan kelas ParkingLot

    def __init__(self, kapasitas="", jumlahKendaraanSekarang=""):
        self.kapasitas = kapasitas
        self.jumlahKendaraanSekarang = jumlahKendaraanSekarang

    # mengeset dan mengembalikan atribut-atribut pada kelas ParkingLot
    def setKapasitas(self, kapasitas):
        self.kapasitas = kapasitas

    def getKapasitas(self):
        return self.kapasitas
    
    def setJumlahKendaraanSekarang(self, jumlahKendaraanSekarang):
        self.jumlahKendaraanSekarang = jumlahKendaraanSekarang

    def getJumlahKendaraanSekarang(self):
        return self.jumlahKendaraanSekarang