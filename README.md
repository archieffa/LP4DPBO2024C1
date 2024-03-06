# JANJI

Saya Syifa Azzahra NIM 2207308 mengerjakan soal Latihan 4 dalam mata kuliah
Desain Pemrograman Berorientasi Objek untuk keberkahan-Nya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

# DESKRIPSI TUGAS

Buatlah program berbasis OOP menggunakan bahasa pemrograman C++ dan Python
yang mengimplementasikan konsep inheritance, composition, dan array of object
pada kelas-kelas berikut :

1. Vehicle : plat nomor, merk, tahun produksi, warna
2. Car : jumlah kursi, jumlah pintu
3. Motorcycle : jenis motor, kapasitas tangki
4. Garage : nama garasi, luas garasi, daftar kendaraan
5. ParkingLot : kapasitas, jumlah kendaraan saat ini

# DESAIN KELAS (DIAGRAM)
![uml_latprak4](https://github.com/archieffa/LP4DPBO2024C1/assets/121290445/1e30d6cb-df76-4b88-b37c-d4df64631933)

# DESAIN KODE PROGRAM

Program ini menggunakan lima kelas yaitu:

1. Class Vehicle (Super/Base Class)
    
    Kelas ini menjadi Parent Class untuk Class Car dan Motorcycle. Kelas ini memiliki empat atribut, yaitu:
    
    - platNomor: menyimpan plat nomor dalam bentuk string
    - merk: menyimpan merk dalam bentuk string
    - tahunProduksi: menyimpan tahun produksi dalam bentuk string
    - warna: menyimpan warna dalam bentuk string
2. Class Car
    
    Kelas ini menjadi Child Class untuk Class Vehicle. Kelas ini memiliki tiga atribut, yaitu:
    
    - jenisMobil: menyimpan jenis mobil dalam bentuk string
    - jumlahKursi: menyimpan jumlah kursi dalam bentuk string
    - jumlahPintu: menyimpan jumlah pintu dalam bentuk string
3. Class Motorcycle
    
    Kelas ini menjadi Child Class untuk Class Vehicle. Kelas ini memiliki dua atribut, yaitu:
    
    - jenisMotor: menyimpan jenis motor dalam bentuk string
    - kapasitasTangki: menyimpan kapasitas tangki dalam bentuk string
4. Class Garage
    
    Kelas ini mengcomposite Class Car dan Class Motorcycle. Kelas ini memiliki empat atribut, yaitu:
    
    - namaGarasi: menyimpan nama garasi dalam bentuk string
    - luasGarasi: menyimpan luas garasi dalam bentuk string
    - car: menyimpan array data mobil dalam bentuk list atau vector.
    - motorcycle: menyimpan array data motor dalam bentuk list atau vector.
5. Class ParkingLot
    
    Kelas ini mengcomposite Class Car dan Class Motorcycle. Kelas ini memiliki empat atribut, yaitu:
    
    - jenisMotor: menyimpan jenis motor dalam bentuk string
    - kapasitasTangki: menyimpan kapasitas tangki dalam bentuk string
    - car: menyimpan array data mobil dalam bentuk list atau vector.
    - motorcycle: menyimpan array data motor dalam bentuk list atau vector.

Kelima kelas diatas memiliki setter dan getter untuk setiap atributnya. Penyimpanan data clothing brand menggunakan struktur data list.

# ALUR PROGRAM

Pada program Main, inputan datanya berupa hardcode. Pertama adalah menambahkan lalu menampilkan data mobil dan motor yang ada di garasi. Selain menampilkan data mobil dan motor juga menampilkan data garasi itu sendiri. Selanjutnya adalah menambahkan lalu menampilkan data mobil dan motor yang ada di tempat parkir. Selain menampilkan data mobil dan motor juga menampilkan data tempat parkir itu sendiri.

# DOKUMENTASI
## PYTHON_UPDATE
![garasi](https://github.com/archieffa/LP4DPBO2024C1/assets/121290445/4aeb8394-5b8d-4e02-86b1-a15c3b326aea)
![tempatParkir](https://github.com/archieffa/LP4DPBO2024C1/assets/121290445/ebd59206-b9fb-4a00-a518-784ca91dd2cd)

## c++
![garasi](https://github.com/archieffa/LP4DPBO2024C1/assets/121290445/3811263e-f6e0-4114-8ef9-9b714e4c03ea)
![tempatParkir](https://github.com/archieffa/LP4DPBO2024C1/assets/121290445/a1e3d492-a77c-45d4-9da5-941280951c60)
