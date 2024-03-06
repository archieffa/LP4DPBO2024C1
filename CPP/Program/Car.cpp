/* Saya Syifa Azzahra NIM 2207308 mengerjakan soal Latihan 4 dalam mata kuliah 
Desain Pemrograman Berorientasi Objek untuk keberkahan-Nya maka saya tidak melakukan kecurangan seperti yang telah
dispesifikasikan. Aamiin. */

#pragma once

#include <string>
#include <iostream>
#include <vector>
#include "Vehicle.cpp"

using namespace std;

class Car : public Vehicle 
{
    private:
        string jenisMobil;
        string jumlahKursi;
        string jumlahPintu;

    public:

        // Konstruktor
        Car(string platNomor, string merk, string tahunProduksi, string warna, string jenisMobil, string jumlahKursi, string jumlahPintu)
            : Vehicle(platNomor, merk, tahunProduksi, warna), jenisMobil(jenisMobil), jumlahKursi(jumlahKursi), jumlahPintu(jumlahPintu) 
            {
                this->jenisMobil = jenisMobil;
                this->jumlahKursi = jumlahKursi;
                this->jumlahPintu = jumlahPintu;
            }

        // Getter dan Setter untuk JenisMobil
        void setJenisMobil(string jenisMobil) 
        {
            this->jenisMobil = jenisMobil;
        }

        string getJenisMobil() 
        {
            return this->jenisMobil;
        }

        // Getter dan Setter untuk JumlahKursi
        void setJumlahKursi(string jumlahKursi) 
        {
            this->jumlahKursi = jumlahKursi;
        }

        string getJumlahKursi() 
        {
            return this->jumlahKursi;
        }

        // Getter dan Setter untuk JumlahPintu
        void setJumlahPintu(string jumlahPintu) 
        {
            this->jumlahPintu = jumlahPintu;
        }

        string getJumlahPintu() 
        {
            return this->jumlahPintu;
        }

        ~Car()
        {

        }
};