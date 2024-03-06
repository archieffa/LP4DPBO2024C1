/* Saya Syifa Azzahra NIM 2207308 mengerjakan soal Latihan 4 dalam mata kuliah 
Desain Pemrograman Berorientasi Objek untuk keberkahan-Nya maka saya tidak melakukan kecurangan seperti yang telah
dispesifikasikan. Aamiin. */

#pragma once

#include <string>
#include <iostream>
#include <vector>
#include "Vehicle.cpp"

using namespace std;

class Motorcycle : public Vehicle 
{
    private:
        string jenisMotor;
        string kapasitasTangki;

    public:
        // Konstruktor
        Motorcycle(string platNomor, string merk, string tahunProduksi, string warna, string jenisMotor, string kapasitasTangki)
            : Vehicle(platNomor, merk, tahunProduksi, warna), jenisMotor(jenisMotor), kapasitasTangki(kapasitasTangki) 
            {

            }

        // Getter dan Setter untuk jenisMotor
        void setJenisMotor(string jenisMotor) 
        {
            this->jenisMotor = jenisMotor;
        }

        string getJenisMotor() 
        {
            return this->jenisMotor;
        }

        // Getter dan Setter untuk KapasitasTangki
        void setKapasitasTangki(string kapasitasTangki) 
        {
            this->kapasitasTangki = kapasitasTangki;
        }

        string getKapasitasTangki() 
        {
            return this->kapasitasTangki;
        }

        ~Motorcycle()
        {

        }
};