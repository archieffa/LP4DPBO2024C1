# Saya Syifa Azzahra NIM 2207308 mengerjakan soal Latihan 4 dalam mata kuliah 
# Desain Pemrograman Berorientasi Objek untuk keberkahan-Nya maka saya tidak melakukan kecurangan seperti yang telah
# dispesifikasikan. Aamiin. 

class Garage:
# kelas yang digunakan untuk mengimplementasikan kelas Garage 
    
    namaGarasi = ""
    luasGarasi = ""
    car = []
    motorcycle = []

    def __init__(self, namaGarasi, luasGarasi):
        self.namaGarasi = namaGarasi
        self.luasGarasi = luasGarasi
    
    # mengeset dan mengembalikan atribut-atribut pada kelas Garage
    def setNamaGarasi(self, namaGarasi):
        self.namaGarasi = namaGarasi

    def getNamaGarasi(self):
        return self.namaGarasi
    
    def setLuasGarasi(self, luasGarasi):
        self.luasGarasi = luasGarasi

    def getLuasGarasi(self):
        return self.luasGarasi
    
    
    def setCar(self, car):
        self.car = car

    def getCar(self):
        return self.car
    
    def setMotorcycle(self, motorcycle):
        self.motorcycle = motorcycle

    def getMotorcycle(self):
        return self.motorcycle