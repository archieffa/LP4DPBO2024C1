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

class Garage 
{
    private:
        string namaGarasi;
        string luasGarasi;
        vector<Car> car;
        vector<Motorcycle> motorcycle;

    public:
        // Konstruktor
        Garage(string namaGarasi, string luasGarasi) : namaGarasi(namaGarasi), luasGarasi(luasGarasi) 
        {

        }

        // Getter dan Setter untuk namaGarasi
        void setNamaGarasi(string namaGarasi) 
        {
            this->namaGarasi = namaGarasi;
        }

        string getNamaGarasi() 
        {
            return this->namaGarasi;
        }

        // Getter dan Setter untuk luasGarasi
        void setLuasGarasi(string luasGarasi) 
        {
            this->luasGarasi = luasGarasi;
        }

        string getLuasGarasi() 
        {
            return this->luasGarasi;
        }

        // Getter dan Setter untuk car
        void setCar(vector<Car> car) 
        {
            this->car = car;
        }

        vector<Car> getCar() {
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

        ~Garage()
        {
            
        }
};