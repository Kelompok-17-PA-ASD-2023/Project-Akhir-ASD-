# Project Akhir ASD Kelompok 17
Anggota kelompok: 
- Vera Santi Wijaya
- Lidia Aprilia Putri
- Juventia Adelia Putri 

## Deskripsi Program
- Berikut adalah program project kelompok kami dengan tema lowongan pekerjaan. Tujuan dibuatnya program ini untuk mengelola informasi mengenai lowongan pekerjaan di suatu perusahaan yang meliputi posisi kerja, nama perusahaan, nominal gaji, domisili perusahaan, dan maksimal umur pelamar kerja. Program kami menggunakan database Mongodb untuk menyimpan data-data lowongan pekerjaan diatas. 

-  Pada program kami, terdapat 2 user dengan privilege yang berbeda. Pertama, user admin. Admin memiliki privilege untuk menampilkan seluruh data loker, menambahkan data loker, menghapus data loker, dan melihat seluruh user pelamar. Kedua, user pelamar. Pelamar memiliki privilege untuk melihat daftar data loker, mencari data loker, mengurutkan data loker berdasarkan gaji dari yang terbesar, dan data profil pelamar

## Struktur Project

![Cuplikan layar 2023-04-27 012912](https://user-images.githubusercontent.com/122012870/234656205-60120f74-8c3d-41e9-bfd6-e5917bebce2a.png)

mvc

## Fitur dan Fungsionalitas

### Dalam Folder Controller
![Cuplikan layar 2023-04-27 013252](https://user-images.githubusercontent.com/122012870/234656715-b3cd74fc-708f-480c-9340-c0355f9378ce.png)
#### 👩‍💻 File ControlAccount
- Mengimport Module dan Library

Mengimport module berfungsi sebagai multi file yaitu agar dapat memanggil file lain di dalam satu module yang berbeda, pada file ini file lain yang dipanggil ialah file database dari folder Model dan file viewadmin serta file viewpelamar yang masing-masingnya berasal dari folder View

Mengimport library dimaksudkan untuk memanfaatkan fungsionalitas dalam library tersebut untuk kebutuhan tertentu, di dalam program ini library yang digunakan adalah library pwinput yang bertugas mengenkripsikan password yang diinput pengguna, kemudian library os yang bertugas untuk melakukan berbagai macam operasi yang terkait dengan sistem operasi, dan yang terakhir adalah library time yang bertugas untuk melakukan operasi yang berkaitan dengan waktu dan tanggal

![Cuplikan layar 2023-04-27 013514](https://user-images.githubusercontent.com/122012870/234657400-009c2264-0de2-412f-8adf-914dba999984.png)

- Function Login

Fungsi Login adalah program yang digunakan untuk menampilkan perintah terkait login sebelum masuk ke dalam aplikasi, di dalamnya terdapat percabangan(if, elif, else) yang digunakan untuk mengeksekusi kode tertentu hanya jika kondisi tersebut terpenuhi. 

Di dalam penginputan juga terdapat metode bawaan python diantara adalah lower yang merupakan metode untuk mengubah seluruh karakter menjadi huruf kecil dan capitalize yang merupakan metode untuk mengubah karakter pertama dalam string menjadi huruf kapital sedangkan karakter lainnya adalah huruf kecil.

Untuk mencari nama yang sesuai dalam database maka diperlukan find_one, find_one sendiri ialah salah satu metode dalam Mongodb yang selanjutnya hasil pencarian tersebut akan tersimpan dalam variabel result 

Penggunaan statement try except dimaksudkan untuk menangani kesalahan penginputan data dari user yang tidak disengaja agar tidak terjadi error di dalam output program nantinya

![Cuplikan layar 2023-04-27 020119](https://user-images.githubusercontent.com/122012870/234663647-b2094070-0f16-4fa2-83fa-56c5d81049ba.png)

- Function profilpelamar

Function profilpelamar adalah program yang menampilkan perintah terkait dengan data-data si pelamar yang telah tersimpan dalam database, menggunakan metode find_one untuk mencari data sesuai nama pelamar yang sedang login

![Cuplikan layar 2023-04-27 021628](https://user-images.githubusercontent.com/122012870/234666697-941e61ff-e499-4853-b0c1-95b6742b12cf.png)

#### 👩‍💻 File ControlLoker
- Mengimport Module dan Library

Mengimport module berfungsi sebagai multi file yaitu agar dapat memanggil file lain di dalam satu module yang berbeda, pada file ini file lain yang dipanggil ialah file database dari folder Model 

Mengimport library dimaksudkan untuk memanfaatkan fungsionalitas dalam library tersebut untuk kebutuhan tertentu, di dalam program ini library yang digunakan adalah library prettytable yang bertugas untuk menyusun data ke dalam tabel-tabel agar terlihat rapi dan mudah dibaca, serta ada library os yang bertugas untuk melakukan berbagai macam operasi yang terkait dengan sistem operasi.

![Cuplikan layar 2023-04-27 023551](https://user-images.githubusercontent.com/122012870/234670919-24167021-8171-4b6b-b54a-ef49648ce850.png)

- Class Node

Class Node adalah untuk mempresentasikan sebuah simpul dalam Linked list

![Cuplikan layar 2023-04-27 023707](https://user-images.githubusercontent.com/122012870/234671236-a7c58ade-dc56-4388-bfba-613382e52277.png)

- Class LinkedList

Class LinkedList adalah salah satu struktur data yang yang terdiri dari node-node yang terhubung satu sama lain. Dalam Class LinkedList, fungsi def init dan self berperan sebagai konstruktor untuk membuat instance dari class tersebut

![Cuplikan layar 2023-04-27 024025](https://user-images.githubusercontent.com/122012870/234671866-77591dd2-fde7-4c09-8430-bb6f45e264c3.png)

- Method append

Method ini berfungsi untuk menambahkan node baru di bagian akhir linked list. Method kemudian akan membuat istance baru dari class Node dan menyimpan data pada node tersebut. Di dalam kurung method terdapat parameter self yang digunakan oleh seluruh method di dalam Class LinkedList

![Cuplikan layar 2023-04-27 024623](https://user-images.githubusercontent.com/122012870/234673292-dacdf10c-4dea-497d-b0fe-0e7b40709897.png)

- Method add_data

Method ini berfungsi untuk menambahkan data yang sesuai dengan penempatannya dengan database ke dalam method append. Di dalam kurung method terdapat parameter self yang digunakan oleh seluruh method di dalam Class LinkedList

![Cuplikan layar 2023-04-27 025431](https://user-images.githubusercontent.com/122012870/234675096-bb1e1734-bea4-468f-812c-44bb54b30292.png)





