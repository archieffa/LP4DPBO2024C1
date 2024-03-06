/* Saya Syifa Azzahra NIM 2207308 mengerjakan soal Latihan 4 dalam mata kuliah 
Desain Pemrograman Berorientasi Objek untuk keberkahan-Nya maka saya tidak melakukan kecurangan seperti yang telah
dispesifikasikan. Aamiin. */

#pragma once

#include <iostream>
#include <string>

using namespace std;

class Vehicle 
{
    private:
        string platNomor;
        string merk;
        string tahunProduksi;
        string warna;

    public:
        Vehicle()
        {

        }

        // Konstruktor
        Vehicle(string platNomor="", string merk="", string tahunProduksi="", string warna="") 
        {
            this->platNomor = platNomor;
            this->merk = merk;
            this->tahunProduksi = tahunProduksi;
            this->warna = warna;
        }

        // Getter dan Setter
        void setPlatNomor(string platNomor) 
        {
            this->platNomor = platNomor;
        }

        string getPlatNomor() 
        {
            return this->platNomor;
        }

        void setMerk(string merk) 
        {
            this->merk = merk;
        }

        string getMerk() 
        {
            return this->merk;
        }

        void setTahunProduksi(string tahunProduksi) 
        {
            this->tahunProduksi = tahunProduksi;
        }

        string getTahunProduksi() 
        {
            return this->tahunProduksi;
        }

        void setWarna(string warna) 
        {
            this->warna = warna;
        }

        string getWarna() 
        {
            return this->warna;
        }

        ~Vehicle()
        {
            
        }
};