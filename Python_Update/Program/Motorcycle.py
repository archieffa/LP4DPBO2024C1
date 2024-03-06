# Saya Syifa Azzahra NIM 2207308 mengerjakan soal Latihan 4 dalam mata kuliah 
# Desain Pemrograman Berorientasi Objek untuk keberkahan-Nya maka saya tidak melakukan kecurangan seperti yang telah
# dispesifikasikan. Aamiin. 

from Vehicle import Vehicle

class Motorcycle(Vehicle):
# kelas yang digunakan untuk mengimplementasikan kelas Motorcycle
     
    jenisMotor = ""
    kapasitasTangki = ""
    
    def __init__(self, platNomor, merk, tahunProduksi, warna, jenisMotor, kapasitasTangki):
        super().__init__(platNomor, merk, tahunProduksi, warna)
        self.jenisMotor = jenisMotor
        self.kapasitasTangki = kapasitasTangki

    # mengeset dan mengembalikan atribut-atribut pada kelas Motorcycle
    def setJenisMotor(self, jenisMotor):
        self.jenisMotor = jenisMotor

    def getJenisMotor(self):
        return self.jenisMotor
    
    def setKapasitasTangki(self, kapasitasTangki):
        self.kapasitasTangki = kapasitasTangki

    def getKapasitasTangki(self):
        return self.kapasitasTangki