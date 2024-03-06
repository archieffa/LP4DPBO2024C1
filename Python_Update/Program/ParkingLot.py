# Saya Syifa Azzahra NIM 2207308 mengerjakan soal Latihan 4 dalam mata kuliah 
# Desain Pemrograman Berorientasi Objek untuk keberkahan-Nya maka saya tidak melakukan kecurangan seperti yang telah
# dispesifikasikan. Aamiin. 

class ParkingLot:
# kelas yang digunakan untuk mengimplementasikan kelas ParkingLot
    
    namaParkingLot = ""
    kapasitas = ""
    jumlahKendaraanSaatIni = ""
    car = []
    motorcycle = []

    def __init__(self, namaParkingLot, jumlahKendaraanSaatIni, kapasitas):
        self.namaParkingLot = namaParkingLot
        self.kapasitas = kapasitas
        self.jumlahKendaraanSaatIni = jumlahKendaraanSaatIni

    # mengeset dan mengembalikan atribut-atribut pada kelas ParkingLot
    def setNamaParkingLot(self, namaParkingLot):
        self.namaParkingLot = namaParkingLot

    def getNamaParkingLot(self):
        return self.namaParkingLot
    
    def setKapasitas(self, kapasitas):
        self.kapasitas = kapasitas

    def getKapasitas(self):
        return self.kapasitas
    
    def setJumlahKendaraanSaatIni(self, jumlahKendaraanSaatIni):
        self.jumlahKendaraanSaatIni = jumlahKendaraanSaatIni

    def getJumlahKendaraanSaatIni(self):
        return self.jumlahKendaraanSaatIni
    
    
    def setCar(self, car):
        self.car = car

    def getCar(self):
        return self.car
    
    def setMotorcycle(self, motorcycle):
        self.motorcycle = motorcycle

    def getMotorcycle(self):
        return self.motorcycle