/* Saya Syifa Azzahra NIM 2207308 mengerjakan soal Latihan 4 dalam mata kuliah 
Desain Pemrograman Berorientasi Objek untuk keberkahan-Nya maka saya tidak melakukan kecurangan seperti yang telah
dispesifikasikan. Aamiin. */

#include <bits/stdc++.h>
#include "Vehicle.cpp"
#include "Car.cpp"
#include "Motorcycle.cpp"
#include "Garage.cpp"
#include "ParkingLot.cpp"

using namespace std;

int main() 
{
    // Membuat beberapa instance dari kelas Car
    Car car1("B 1234 CD", "Toyota", "2020", "Hitam", "Sedan", "5", "4");
    Car car2("B 5678 EF", "Honda", "2018", "Putih", "SUV", "7", "4");
    Car car3("B 9876 GH", "Mitsubishi", "2019", "Merah", "MPV", "8", "4");
    Car car4("B 4567 IJ", "Ford", "2017", "Biru", "Hatchback", "5", "5");

    // Membuat beberapa instance dari kelas Motorcycle
    Motorcycle motorcycle1("B 9876 AB", "Yamaha", "2019", "Merah", "Sport", "10");
    Motorcycle motorcycle2("B 5432 CD", "Suzuki", "2021", "Hitam", "Matic", "8");
    Motorcycle motorcycle3("B 1234 EF", "Honda", "2020", "Putih", "Cub", "1");
    Motorcycle motorcycle4("B 6789 GH", "Kawasaki", "2018", "Hijau", "Naked", "12");

    // Membuat instance dari kelas Garage
    Garage garage("Garasi SEVENTEEN", "10x10m");

    // Menambahkan mobil dan sepeda motor ke dalam garasi
    vector<Car> car = {car1, car2};
    vector<Motorcycle> motorcycle = {motorcycle1, motorcycle2};
    garage.setCar(car);
    garage.setMotorcycle(motorcycle);

    // Menampilkan informasi garasi
    cout << endl << "===== INFORMASI GARASI =====" << endl << endl;
    cout << "- Nama Garasi: " << garage.getNamaGarasi() << endl;
    cout << "- Luas Garasi: " << garage.getLuasGarasi() << endl;
    cout << "- Mobil di Garasi:" << endl;
    vector<Car> cars = garage.getCar();
    for (size_t i = 0; i < cars.size(); ++i) {
        Car car = cars[i];
        cout << "  > Plat Nomor: " << car.getPlatNomor() << endl;
        cout << "    Merk: " << car.getMerk() << endl;
        cout << "    Tahun Produksi: " << car.getTahunProduksi() << endl;
        cout << "    Warna: " << car.getWarna() << endl;
        cout << "    Jenis Mobil: " << car.getJenisMobil() << endl;
        cout << "    Jumlah Kursi: " << car.getJumlahKursi() << endl;
        cout << "    Jumlah Pintu: " << car.getJumlahPintu() << endl;
    }

    cout << "- Sepeda Motor di Garasi:" << endl;
    vector<Motorcycle> motorcycles = garage.getMotorcycle();
    for (size_t i = 0; i < motorcycles.size(); ++i) {
        Motorcycle motorcycle = motorcycles[i];
        cout << "  > Plat Nomor: " << motorcycle.getPlatNomor() << endl;
        cout << "    Merk: " << motorcycle.getMerk() << endl;
        cout << "    Tahun Produksi: " << motorcycle.getTahunProduksi() << endl;
        cout << "    Warna: " << motorcycle.getWarna() << endl;
        cout << "    Jenis Motor: " << motorcycle.getJenisMotor() << endl;
        cout << "    Kapasitas Tangki: " << motorcycle.getKapasitasTangki() << endl;
    }
    cout << endl << "============================" << endl << endl;

    // Membuat instance dari kelas ParkingLot
    ParkingLot parking_lot("Tempat Parkir CARAT", "4", "50");

    // Menambahkan mobil dan sepeda motor ke dalam tempat parkir
    car = {car3, car4};
    motorcycle = {motorcycle3, motorcycle4};
    parking_lot.setCar(car);
    parking_lot.setMotorcycle(motorcycle);

    // Menampilkan informasi tempat parkir
    cout << endl << endl << "===== INFORMASI TEMPAT PARKIR =====" << endl << endl;
    cout << "- Nama Tempat Parkir: " << parking_lot.getNamaParkingLot() << endl;
    cout << "- Kapasitas Tempat Parkir: " << parking_lot.getKapasitas() << endl;
    cout << "- Jumlah Kendaraan Saat Ini: " << parking_lot.getJumlahKendaraanSaatIni() << endl;
    cout << "- Mobil di Tempat Parkir:" << endl;
    vector<Car> Cars = parking_lot.getCar();
    for (size_t i = 0; i < Cars.size(); ++i) {
        Car car = Cars[i];
        cout << "  > Plat Nomor: " << car.getPlatNomor() << endl;
        cout << "    Merk: " << car.getMerk() << endl;
        cout << "    Tahun Produksi: " << car.getTahunProduksi() << endl;
        cout << "    Warna: " << car.getWarna() << endl;
        cout << "    Jenis Mobil: " << car.getJenisMobil() << endl;
        cout << "    Jumlah Kursi: " << car.getJumlahKursi() << endl;
        cout << "    Jumlah Pintu: " << car.getJumlahPintu() << endl;
    }

    cout << "- Sepeda Motor di Tempat Parkir:" << endl;
    vector<Motorcycle> Motorcycles = parking_lot.getMotorcycle();
    for (size_t i = 0; i < Motorcycles.size(); ++i) {
        Motorcycle motorcycle = Motorcycles[i];
        cout << "  > Plat Nomor: " << motorcycle.getPlatNomor() << endl;
        cout << "    Merk: " << motorcycle.getMerk() << endl;
        cout << "    Tahun Produksi: " << motorcycle.getTahunProduksi() << endl;
        cout << "    Warna: " << motorcycle.getWarna() << endl;
        cout << "    Jenis Motor: " << motorcycle.getJenisMotor() << endl;
        cout << "    Kapasitas Tangki: " << motorcycle.getKapasitasTangki() << endl;
    }
    cout << endl << "===================================" << endl;

    return 0;
}