# Saya Syifa Azzahra NIM 2207308 mengerjakan soal Latihan 4 dalam mata kuliah 
# Desain Pemrograman Berorientasi Objek untuk keberkahan-Nya maka saya tidak melakukan kecurangan seperti yang telah
# dispesifikasikan. Aamiin. 

from Vehicle import Vehicle
from Car import Car
from Motorcycle import Motorcycle
from VehicleStorage import VehicleStorage
from Garage import Garage
from ParkingLot import ParkingLot

# tabel untuk data mobil
def tampilanTabelCar(car_list):
    if not car_list:
        print("\nData kosong.\n")
        return

    # Inisialisasi panjang maksimum tiap kolom dengan panjang header
    panjangMaxPlatNomor = len("Plat Nomor")
    panjangMaxMerk = len("Merk")
    panjangMaxTahunProduksi = len("Tahun Produksi")
    panjangMaxWarna = len("Warna")
    panjangMaxJenisMobil = len("Jenis Mobil")
    panjangMaxJumlahKursi = len("Jumlah Kursi")
    panjangMaxJumlahPintu = len("Jumlah Pintu")
    panjangMaxNamaVehicleStorage = len("Nama Tempat")
    panjangMaxLokasi = len("Lokasi")

    # Mencari panjang maksimum untuk tiap kolom dari data mobil
    for vehicle in car_list:
        panjangMaxPlatNomor = max(panjangMaxPlatNomor, len(vehicle.getPlatNomor()))
        panjangMaxMerk = max(panjangMaxMerk, len(vehicle.getMerk()))
        panjangMaxTahunProduksi = max(panjangMaxTahunProduksi, len(vehicle.getTahunProduksi()))
        panjangMaxWarna = max(panjangMaxWarna, len(vehicle.getWarna()))
        panjangMaxJenisMobil = max(panjangMaxJenisMobil, len(vehicle.getJenisMobil()))
        panjangMaxJumlahKursi = max(panjangMaxJumlahKursi, len(vehicle.getJumlahKursi()))
        panjangMaxJumlahPintu = max(panjangMaxJumlahPintu, len(vehicle.getJumlahPintu()))
        panjangMaxNamaVehicleStorage = max(panjangMaxNamaVehicleStorage, len(vehicle.getNamaVehicleStorage())) if hasattr(vehicle, 'namaVehicleStorage') else panjangMaxNamaVehicleStorage
        panjangMaxLokasi = max(panjangMaxLokasi, len(vehicle.getLokasi())) if hasattr(vehicle, 'lokasi') else panjangMaxLokasi

    # Menampilkan tabel dengan lebar kolom yang sesuai
    print("\n+-" + "-" * panjangMaxPlatNomor + "-+-" + "-" * panjangMaxMerk + "-+-" + "-" * panjangMaxTahunProduksi + "-+-" + "-" * panjangMaxWarna + "-+-" + "-" * panjangMaxJenisMobil + "-+-" + "-" * panjangMaxJumlahKursi + "-+-" + "-" * panjangMaxJumlahPintu + "-+-" + "-" * panjangMaxNamaVehicleStorage + "-+-" + "-" * panjangMaxLokasi + "-+")
    print("| {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} |".format("Plat Nomor", panjangMaxPlatNomor, "Merk", panjangMaxMerk, "Tahun Produksi", panjangMaxTahunProduksi, "Warna", panjangMaxWarna, "Jenis Mobil", panjangMaxJenisMobil, "Jumlah Kursi", panjangMaxJumlahKursi, "Jumlah Pintu", panjangMaxJumlahPintu, "Nama Tempat", panjangMaxNamaVehicleStorage, "Lokasi", panjangMaxLokasi))
    print("+-" + "-" * panjangMaxPlatNomor + "-+-" + "-" * panjangMaxMerk + "-+-" + "-" * panjangMaxTahunProduksi + "-+-" + "-" * panjangMaxWarna + "-+-" + "-" * panjangMaxJenisMobil + "-+-" + "-" * panjangMaxJumlahKursi + "-+-" + "-" * panjangMaxJumlahPintu + "-+-" + "-" * panjangMaxNamaVehicleStorage + "-+-" + "-" * panjangMaxLokasi + "-+")

    # Menampilkan data mobil
    for vehicle in car_list:
        print("| {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} |".format(vehicle.getPlatNomor(), panjangMaxPlatNomor, vehicle.getMerk(), panjangMaxMerk, vehicle.getTahunProduksi(), panjangMaxTahunProduksi, vehicle.getWarna(), panjangMaxWarna, vehicle.getJenisMobil(), panjangMaxJenisMobil, vehicle.getJumlahKursi(), panjangMaxJumlahKursi, vehicle.getJumlahPintu(), panjangMaxJumlahPintu, vehicle.getNamaVehicleStorage(), panjangMaxNamaVehicleStorage, vehicle.getLokasi(), panjangMaxLokasi))

    # Menampilkan garis pembatas
    print("+-" + "-" * panjangMaxPlatNomor + "-+-" + "-" * panjangMaxMerk + "-+-" + "-" * panjangMaxTahunProduksi + "-+-" + "-" * panjangMaxWarna + "-+-" + "-" * panjangMaxJenisMobil + "-+-" + "-" * panjangMaxJumlahKursi + "-+-" + "-" * panjangMaxJumlahPintu + "-+-" + "-" * panjangMaxNamaVehicleStorage + "-+-" + "-" * panjangMaxLokasi + "-+")

# tabel untuk data motor
def tampilanTabelMotorcycle(motorcycle_list):
    if not motorcycle_list:
        print("\nData kosong.\n")
        return

    # Inisialisasi panjang maksimum tiap kolom dengan panjang header
    panjangMaxPlatNomor = len("Plat Nomor")
    panjangMaxMerk = len("Merk")
    panjangMaxTahunProduksi = len("Tahun Produksi")
    panjangMaxWarna = len("Warna")
    panjangMaxJenisMotor = len("Jenis Motor")
    panjangMaxKapasitasTangki = len("Kapasitas Tangki")
    panjangMaxNamaVehicleStorage = len("Nama Tempat")
    panjangMaxLokasi = len("Lokasi")

    # Mencari panjang maksimum untuk tiap kolom dari data motor
    for vehicle in motorcycle_list:
        panjangMaxPlatNomor = max(panjangMaxPlatNomor, len(vehicle.getPlatNomor()))
        panjangMaxMerk = max(panjangMaxMerk, len(vehicle.getMerk()))
        panjangMaxTahunProduksi = max(panjangMaxTahunProduksi, len(vehicle.getTahunProduksi()))
        panjangMaxWarna = max(panjangMaxWarna, len(vehicle.getWarna()))
        panjangMaxJenisMotor = max(panjangMaxJenisMotor, len(vehicle.getJenisMotor()))
        panjangMaxKapasitasTangki = max(panjangMaxKapasitasTangki, len(vehicle.getKapasitasTangki()))
        panjangMaxNamaVehicleStorage = max(panjangMaxNamaVehicleStorage, len(vehicle.getNamaVehicleStorage())) if hasattr(vehicle, 'namaVehicleStorage') else panjangMaxNamaVehicleStorage
        panjangMaxLokasi = max(panjangMaxLokasi, len(vehicle.getLokasi())) if hasattr(vehicle, 'lokasi') else panjangMaxLokasi

    # Menampilkan tabel dengan lebar kolom yang sesuai
    print("\n+-" + "-" * panjangMaxPlatNomor + "-+-" + "-" * panjangMaxMerk + "-+-" + "-" * panjangMaxTahunProduksi + "-+-" + "-" * panjangMaxWarna + "-+-" + "-" * panjangMaxJenisMotor + "-+-" + "-" * panjangMaxKapasitasTangki + "-+-" + "-" * panjangMaxNamaVehicleStorage + "-+-" + "-" * panjangMaxLokasi + "-+")
    print("| {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} |".format("Plat Nomor", panjangMaxPlatNomor, "Merk", panjangMaxMerk, "Tahun Produksi", panjangMaxTahunProduksi, "Warna", panjangMaxWarna, "Jenis Motor", panjangMaxJenisMotor, "Kapasitas Tangki", panjangMaxKapasitasTangki, "Nama Tempat", panjangMaxNamaVehicleStorage, "Lokasi", panjangMaxLokasi))
    print("+-" + "-" * panjangMaxPlatNomor + "-+-" + "-" * panjangMaxMerk + "-+-" + "-" * panjangMaxTahunProduksi + "-+-" + "-" * panjangMaxWarna + "-+-" + "-" * panjangMaxJenisMotor + "-+-" + "-" * panjangMaxKapasitasTangki + "-+-" + "-" * panjangMaxNamaVehicleStorage + "-+-" + "-" * panjangMaxLokasi + "-+")

    # Menampilkan data motor
    for vehicle in motorcycle_list:
        print("| {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} |".format(vehicle.getPlatNomor(), panjangMaxPlatNomor, vehicle.getMerk(), panjangMaxMerk, vehicle.getTahunProduksi(), panjangMaxTahunProduksi, vehicle.getWarna(), panjangMaxWarna, vehicle.getJenisMotor(), panjangMaxJenisMotor, vehicle.getKapasitasTangki(), panjangMaxKapasitasTangki, vehicle.getNamaVehicleStorage(), panjangMaxNamaVehicleStorage, vehicle.getLokasi(), panjangMaxLokasi))

    # Menampilkan garis pembatas
    print("+-" + "-" * panjangMaxPlatNomor + "-+-" + "-" * panjangMaxMerk + "-+-" + "-" * panjangMaxTahunProduksi + "-+-" + "-" * panjangMaxWarna + "-+-" + "-" * panjangMaxJenisMotor + "-+-" + "-" * panjangMaxKapasitasTangki + "-+-" + "-" * panjangMaxNamaVehicleStorage + "-+-" + "-" * panjangMaxLokasi + "-+")

# tabel untuk data tempat penyimpanan kendaraan
def tampilanTabelMotorcycle(motorcycle_list):
    if not motorcycle_list:
        print("\nData kosong.\n")
        return

    # Inisialisasi panjang maksimum tiap kolom dengan panjang header
    panjangMaxPlatNomor = len("Plat Nomor")
    panjangMaxMerk = len("Merk")
    panjangMaxTahunProduksi = len("Tahun Produksi")
    panjangMaxWarna = len("Warna")
    panjangMaxJenisMotor = len("Jenis Motor")
    panjangMaxKapasitasTangki = len("Kapasitas Tangki")
    panjangMaxNamaVehicleStorage = len("Nama Tempat")
    panjangMaxLokasi = len("Lokasi")

    # Mencari panjang maksimum untuk tiap kolom dari data motor
    for vehicle in motorcycle_list:
        panjangMaxPlatNomor = max(panjangMaxPlatNomor, len(vehicle.getPlatNomor()))
        panjangMaxMerk = max(panjangMaxMerk, len(vehicle.getMerk()))
        panjangMaxTahunProduksi = max(panjangMaxTahunProduksi, len(vehicle.getTahunProduksi()))
        panjangMaxWarna = max(panjangMaxWarna, len(vehicle.getWarna()))
        panjangMaxJenisMotor = max(panjangMaxJenisMotor, len(vehicle.getJenisMotor()))
        panjangMaxKapasitasTangki = max(panjangMaxKapasitasTangki, len(vehicle.getKapasitasTangki()))
        panjangMaxNamaVehicleStorage = max(panjangMaxNamaVehicleStorage, len(vehicle.getNamaVehicleStorage())) if hasattr(vehicle, 'namaVehicleStorage') else panjangMaxNamaVehicleStorage
        panjangMaxLokasi = max(panjangMaxLokasi, len(vehicle.getLokasi())) if hasattr(vehicle, 'lokasi') else panjangMaxLokasi

    # Menampilkan tabel dengan lebar kolom yang sesuai
    print("\n+-" + "-" * panjangMaxPlatNomor + "-+-" + "-" * panjangMaxMerk + "-+-" + "-" * panjangMaxTahunProduksi + "-+-" + "-" * panjangMaxWarna + "-+-" + "-" * panjangMaxJenisMotor + "-+-" + "-" * panjangMaxKapasitasTangki + "-+-" + "-" * panjangMaxNamaVehicleStorage + "-+-" + "-" * panjangMaxLokasi + "-+")
    print("| {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} |".format("Plat Nomor", panjangMaxPlatNomor, "Merk", panjangMaxMerk, "Tahun Produksi", panjangMaxTahunProduksi, "Warna", panjangMaxWarna, "Jenis Motor", panjangMaxJenisMotor, "Kapasitas Tangki", panjangMaxKapasitasTangki, "Nama Tempat", panjangMaxNamaVehicleStorage, "Lokasi", panjangMaxLokasi))
    print("+-" + "-" * panjangMaxPlatNomor + "-+-" + "-" * panjangMaxMerk + "-+-" + "-" * panjangMaxTahunProduksi + "-+-" + "-" * panjangMaxWarna + "-+-" + "-" * panjangMaxJenisMotor + "-+-" + "-" * panjangMaxKapasitasTangki + "-+-" + "-" * panjangMaxNamaVehicleStorage + "-+-" + "-" * panjangMaxLokasi + "-+")

    # Menampilkan data motor
    for vehicle in motorcycle_list:
        print("| {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} |".format(vehicle.getPlatNomor(), panjangMaxPlatNomor, vehicle.getMerk(), panjangMaxMerk, vehicle.getTahunProduksi(), panjangMaxTahunProduksi, vehicle.getWarna(), panjangMaxWarna, vehicle.getJenisMotor(), panjangMaxJenisMotor, vehicle.getKapasitasTangki(), panjangMaxKapasitasTangki, vehicle.getNamaVehicleStorage(), panjangMaxNamaVehicleStorage, vehicle.getLokasi(), panjangMaxLokasi))

    # Menampilkan garis pembatas
    print("+-" + "-" * panjangMaxPlatNomor + "-+-" + "-" * panjangMaxMerk + "-+-" + "-" * panjangMaxTahunProduksi + "-+-" + "-" * panjangMaxWarna + "-+-" + "-" * panjangMaxJenisMotor + "-+-" + "-" * panjangMaxKapasitasTangki + "-+-" + "-" * panjangMaxNamaVehicleStorage + "-+-" + "-" * panjangMaxLokasi + "-+")

def tampilanTabelVehicleStorage(vehicleStorage_list):
    if not vehicleStorage_list:
        print("\nData kosong.\n")
        return

    # Fungsi bantuan untuk mengambil panjang maksimum tiap kolom
    def panjangMax(list_of_strings):
        return max(len(str(item)) for item in list_of_strings)

    # Inisialisasi panjang maksimum tiap kolom dengan panjang header
    panjangMaxNamaVehicleStorage = panjangMax(["Nama Tempat"])
    panjangMaxLokasi = panjangMax(["Lokasi"])
    panjangMaxLuasGarasi = panjangMax(["Luas Garasi"])
    panjangMaxDaftarKendaraan = panjangMax(["Daftar Kendaraan"])
    panjangMaxKapasitas = panjangMax(["Kapasitas"])
    panjangMaxJumlahKendaraanSekarang = panjangMax(["Jumlah Kendaraan Sekarang"])

    # Mencari panjang maksimum untuk tiap kolom dari data vehicle storage
    for storage in vehicleStorage_list:
        panjangMaxNamaVehicleStorage = max(panjangMaxNamaVehicleStorage, len(str(storage.getNamaVehicleStorage())))
        panjangMaxLokasi = max(panjangMaxLokasi, len(str(storage.getLokasi())))
        if storage.getGarage():
            panjangMaxLuasGarasi = max(panjangMaxLuasGarasi, len(str(storage.getGarage().getLuasGarasi())))
            panjangMaxDaftarKendaraan = max(panjangMaxDaftarKendaraan, len(str(storage.getGarage().getDaftarKendaraan())))
        if storage.getParkingLot():
            panjangMaxKapasitas = max(panjangMaxKapasitas, len(str(storage.getParkingLot().getKapasitas())))
            panjangMaxJumlahKendaraanSekarang = max(panjangMaxJumlahKendaraanSekarang, len(str(storage.getParkingLot().getJumlahKendaraanSekarang())))

    # Menampilkan tabel dengan lebar kolom yang sesuai
    print("\n+-" + "-" * panjangMaxNamaVehicleStorage + "-+-" + "-" * panjangMaxLokasi + "-+-" + "-" * panjangMaxLuasGarasi + "-+-" + "-" * panjangMaxDaftarKendaraan + "-+-" + "-" * panjangMaxKapasitas + "-+-" + "-" * panjangMaxJumlahKendaraanSekarang + "-+")
    print("| {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} |".format("Nama Tempat", panjangMaxNamaVehicleStorage, "Lokasi", panjangMaxLokasi, "Luas Garasi", panjangMaxLuasGarasi, "Daftar Kendaraan", panjangMaxDaftarKendaraan, "Kapasitas", panjangMaxKapasitas, "Jumlah Kendaraan Sekarang", panjangMaxJumlahKendaraanSekarang))
    print("+-" + "-" * panjangMaxNamaVehicleStorage + "-+-" + "-" * panjangMaxLokasi + "-+-" + "-" * panjangMaxLuasGarasi + "-+-" + "-" * panjangMaxDaftarKendaraan + "-+-" + "-" * panjangMaxKapasitas + "-+-" + "-" * panjangMaxJumlahKendaraanSekarang + "-+")

    # Menampilkan data vehicle storage
    for storage in vehicleStorage_list:
        nama = storage.getNamaVehicleStorage()
        lokasi = storage.getLokasi()
        luas_garasi = storage.getGarage().getLuasGarasi() if storage.getGarage() else ""
        daftar_kendaraan = storage.getGarage().getDaftarKendaraan() if storage.getGarage() else ""
        kapasitas = storage.getParkingLot().getKapasitas() if storage.getParkingLot() else ""
        jumlah_kendaraan = storage.getParkingLot().getJumlahKendaraanSekarang() if storage.getParkingLot() else ""
        print("| {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} |".format(nama, panjangMaxNamaVehicleStorage, lokasi, panjangMaxLokasi, luas_garasi, panjangMaxLuasGarasi, daftar_kendaraan, panjangMaxDaftarKendaraan, kapasitas, panjangMaxKapasitas, jumlah_kendaraan, panjangMaxJumlahKendaraanSekarang))

    # Menampilkan garis pembatas
    print("+-" + "-" * panjangMaxNamaVehicleStorage + "-+-" + "-" * panjangMaxLokasi + "-+-" + "-" * panjangMaxLuasGarasi + "-+-" + "-" * panjangMaxDaftarKendaraan + "-+-" + "-" * panjangMaxKapasitas + "-+-" + "-" * panjangMaxJumlahKendaraanSekarang + "-+")



def main():
    # Membuat objek Car
    car1 = Car("BC 5678 EF", "Honda", "2020", "Putih", "Sedan", "4", "4", "Garage A", "Jakarta")
    car2 = Car("XY 1234 ZW", "Toyota", "2018", "Hitam", "SUV", "7", "5", "Tempat Parkir B", "Bandung")
    car3 = Car("AB 9999 CD", "Nissan", "2019", "Merah", "Hatchback", "5", "3", "Garage C", "Surabaya")

    # Menampilkan data mobil dalam bentuk tabel
    print("\n\n===================================================== DAFTAR MOBIL =====================================================")
    tampilanTabelCar([car1, car2, car3])

    motor1 = Motorcycle("DA 1234 FG", "Yamaha", "2021", "Biru", "Sport", "10 L", "Tempat Parkir X", "Jakarta")
    motor2 = Motorcycle("FG 5678 HI", "Honda", "2019", "Hitam", "Cruiser", "15 L", "Garage Y", "Bandung")
    motor3 = Motorcycle("IJ 9012 KL", "Kawasaki", "2020", "Merah", "Touring", "20 L", "Tempat Parkir Z", "Surabaya")

    # Menampilkan data mobil dalam bentuk tabel
    print("\n\n================================================= DAFTAR MOTOR =================================================")
    tampilanTabelMotorcycle([motor1, motor2, motor3])

    vehicle_storage1 = VehicleStorage("Garage A", "Jakarta", "100 m2", "BC 5678 EF", 10, 1)
    vehicle_storage2 = VehicleStorage("Tempat Parkir B", "Bandung", "200 m2", "XY 1234 ZW", 20, 1)
    vehicle_storage3 = VehicleStorage("Garage C", "Surabaya", "150 m2", "AB 9999 CD", 15, 1)
    vehicle_storage4 = VehicleStorage("Tempat Parkir X", "Jakarta", "120 m2", "DA 1234 FG", 12, 1)
    vehicle_storage5 = VehicleStorage("Garage Y", "Bandung", "180 m2", "FG 5678 HI", 18, 1)
    vehicle_storage6 = VehicleStorage("Tempat Parkir Z", "Surabaya", "160 m2", "IJ 9012 KL", 16, 1)

    print("\n\n=================================== DAFTAR TEMPAT PENYIMPANAN MOBIL ===================================")
    tampilanTabelVehicleStorage([vehicle_storage1, vehicle_storage2, vehicle_storage3, vehicle_storage4, vehicle_storage5, vehicle_storage6])

if __name__ == "__main__":
    main()