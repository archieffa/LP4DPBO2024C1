/* Saya Syifa Azzahra NIM 2207308 mengerjakan soal Latihan 4 dalam mata kuliah 
Desain Pemrograman Berorientasi Objek untuk keberkahan-Nya maka saya tidak melakukan kecurangan seperti yang telah
dispesifikasikan. Aamiin. */

#pragma once

#include <iostream>
#include <vector>
#include <string>
#include "Car.cpp"
#include "Motorcycle.cpp"

using namespace std;

class ParkingLot {
private:
    string namaParkingLot;
    string kapasitas;
    string jumlahKendaraanSaatIni;
    vector<Car> car;
    vector<Motorcycle> motorcycle;

public:
    // Konstruktor
    ParkingLot(string namaParkingLot, string jumlahKendaraanSaatIni, string kapasitas)
        : namaParkingLot(namaParkingLot), kapasitas(kapasitas), jumlahKendaraanSaatIni(jumlahKendaraanSaatIni) 
        {

        }

    // Getter dan Setter untuk namaParkingLot
    void setNamaParkingLot(string namaParkingLot) 
    {
        this->namaParkingLot = namaParkingLot;
    }

    string getNamaParkingLot() 
    {
        return this->namaParkingLot;
    }

    // Getter dan Setter untuk kapasitas
    void setKapasitas(string kapasitas) 
    {
        this->kapasitas = kapasitas;
    }

    string getKapasitas() 
    {
        return this->kapasitas;
    }

    // Getter dan Setter untuk jumlahKendaraanSaatIni
    void setJumlahKendaraanSaatIni(string jumlahKendaraanSaatIni) 
    {
        this->jumlahKendaraanSaatIni = jumlahKendaraanSaatIni;
    }

    string getJumlahKendaraanSaatIni() 
    {
        return this->jumlahKendaraanSaatIni;
    }

    // Getter dan Setter untuk car
    void setCar(vector<Car> car) 
    {
        this->car = car;
    }

    vector<Car> getCar() 
    {
        return this->car;
    }

    // Getter dan Setter untuk motorcycle
    void setMotorcycle(vector<Motorcycle> motorcycle) 
    {
        this->motorcycle = motorcycle;
    }

    vector<Motorcycle> getMotorcycle() 
    {
        return this->motorcycle;
    }

    ~ParkingLot()
    {
        
    }
};
