# Saya Syifa Azzahra NIM 2207308 mengerjakan soal Latihan 4 dalam mata kuliah 
# Desain Pemrograman Berorientasi Objek untuk keberkahan-Nya maka saya tidak melakukan kecurangan seperti yang telah
# dispesifikasikan. Aamiin.

from Vehicle import Vehicle
from Car import Car
from Motorcycle import Motorcycle
from Garage import Garage
from ParkingLot import ParkingLot

# Membuat beberapa instance dari kelas Car
car1 = Car("B 1234 CD", "Toyota", "2020", "Hitam", "Sedan", "5", "4")
car2 = Car("B 5678 EF", "Honda", "2018", "Putih", "SUV", "7", "4")
car3 = Car("B 9876 GH", "Mitsubishi", "2019", "Merah", "MPV", "8", "4")
car4 = Car("B 4567 IJ", "Ford", "2017", "Biru", "Hatchback", "5", "5")

# Membuat beberapa instance dari kelas Motorcycle
motorcycle1 = Motorcycle("B 9876 AB", "Yamaha", "2019", "Merah", "Sport", "10")
motorcycle2 = Motorcycle("B 5432 CD", "Suzuki", "2021", "Hitam", "Matic", "8")
motorcycle3 = Motorcycle("B 1234 EF", "Honda", "2020", "Putih", "Cub", "1")
motorcycle4 = Motorcycle("B 6789 GH", "Kawasaki", "2018", "Hijau", "Naked", "12")

# Membuat instance dari kelas Garage
garage = Garage("Garasi SEVENTEEN", "10x10m")

# Menambahkan mobil dan sepeda motor ke dalam garasi
garage.setCar([car1, car2])
garage.setMotorcycle([motorcycle1, motorcycle2])

# Menampilkan informasi garasi
print()
print("===== INFORMASI GARASI =====")
print()
print("- Nama Garasi:", garage.getNamaGarasi())
print("- Luas Garasi:", garage.getLuasGarasi())
print("- Mobil di Garasi:")
for car in garage.getCar():
    print("  > Plat Nomor:", car.getPlatNomor())
    print("    Merk:", car.getMerk())
    print("    Tahun Produksi:", car.getTahunProduksi())
    print("    Warna:", car.getWarna())
    print("    Jenis Mobil:", car.getJenisMobil())
    print("    Jumlah Kursi:", car.getJumlahKursi())
    print("    Jumlah Pintu:", car.getJumlahPintu())

print("- Sepeda Motor di Garasi:")
for motorcycle in garage.getMotorcycle():
    print("  > Plat Nomor:", motorcycle.getPlatNomor())
    print("    Merk:", motorcycle.getMerk())
    print("    Tahun Produksi:", motorcycle.getTahunProduksi())
    print("    Warna:", motorcycle.getWarna())
    print("    Jenis Motor:", motorcycle.getJenisMotor())
    print("    Kapasitas Tangki:", motorcycle.getKapasitasTangki())
print()
print("============================")

# Membuat instance dari kelas ParkingLot
parking_lot = ParkingLot("Tempat Parkir CARAT", 4, 50)

# Menambahkan mobil dan sepeda motor ke dalam tempat parkir
parking_lot.setCar([car3, car4])
parking_lot.setMotorcycle([motorcycle3, motorcycle4])

# Menampilkan informasi tempat parkir
print()
print()
print("===== INFORMASI TEMPAT PARKIR =====")
print()
print("- Nama Tempat Parkir:", parking_lot.getNamaParkingLot())
print("- Kapasitas Tempat Parkir:", parking_lot.getKapasitas())
print("- Jumlah Kendaraan Saat Ini:", parking_lot.getJumlahKendaraanSaatIni())
print("- Mobil di Tempat Parkir:")
for car in parking_lot.getCar():
    print("  > Plat Nomor:", car.getPlatNomor())
    print("    Merk:", car.getMerk())
    print("    Tahun Produksi:", car.getTahunProduksi())
    print("    Warna:", car.getWarna())
    print("    Jenis Mobil:", car.getJenisMobil())
    print("    Jumlah Kursi:", car.getJumlahKursi())
    print("    Jumlah Pintu:", car.getJumlahPintu())

print("- Sepeda Motor di Tempat Parkir:")
for motorcycle in parking_lot.getMotorcycle():
    print("  > Plat Nomor:", motorcycle.getPlatNomor())
    print("    Merk:", motorcycle.getMerk())
    print("    Tahun Produksi:", motorcycle.getTahunProduksi())
    print("    Warna:", motorcycle.getWarna())
    print("    Jenis Motor:", motorcycle.getJenisMotor())
    print("    Kapasitas Tangki:", motorcycle.getKapasitasTangki())
print()
print("===================================")