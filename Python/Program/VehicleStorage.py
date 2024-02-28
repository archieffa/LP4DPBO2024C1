# Saya Syifa Azzahra NIM 2207308 mengerjakan soal Latihan 4 dalam mata kuliah 
# Desain Pemrograman Berorientasi Objek untuk keberkahan-Nya maka saya tidak melakukan kecurangan seperti yang telah
# dispesifikasikan. Aamiin. 

from Garage import Garage
from ParkingLot import ParkingLot

class VehicleStorage:
# kelas yang digunakan untuk mengimplementasikan kelas VehicleStorage
    
    def __init__(self, namaVehicleStorage="", lokasi="", luasGarasi="", daftarKendaraan=None, kapasitas=0, jumlahKendaraanSekarang=0):
        self.namaVehicleStorage = namaVehicleStorage
        self.lokasi = lokasi
        self.garage = Garage(luasGarasi, daftarKendaraan)
        self.parkingLot = ParkingLot(kapasitas, jumlahKendaraanSekarang)

    # mengeset dan mengembalikan atribut-atribut pada kelas VehicleStorage
    def setNamaVehicleStorage(self, namaVehicleStorage):
        self.namaVehicleStorage = namaVehicleStorage

    def getNamaVehicleStorage(self):
        return self.namaVehicleStorage
    
    def setLokasi(self, lokasi):
        self.lokasi = lokasi

    def getLokasi(self):
        return self.lokasi
    
    def setGarage(self, garage):
        self.garage = garage

    def getGarage(self):
        return self.garage
    
    def setParkingLot(self, parkingLot):
        self.parkingLot = parkingLot

    def getParkingLot(self):
        return self.parkingLot
