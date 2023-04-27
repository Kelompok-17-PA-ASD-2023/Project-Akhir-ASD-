# Struktur Project
A. MVC:
Model View Controller atau yang dapat disingkat MVC adalah sebuah pola arsitektur dalam membuat sebuah aplikasi dengan cara memisahkan kode menjadi tiga bagian yang terdiri dari:

1. Model
Bagian yang bertugas untuk menyiapkan, mengatur, memanipulasi, dan mengorganisasikan data yang ada di database.
2. View
Bagian yang bertugas untuk menampilkan informasi dalam bentuk Graphical User Interface (GUI).
3. Controller
Bagian yang bertugas untuk menghubungkan serta mengatur model dan view agar dapat saling terhubung.

B. Implementasi MVC pada Program Aplikasi Loker di Repository Github:
Pada program kami, pengimplementasian MVC dilakukan dengan membagi 3 folder di Github, yaitu folder Model, View, dan Controller. 

• Folder Model berisi file python untuk mengakses database Mongodb. 

• Folder View berisi 2 file python, yaitu viewadmin dan viewpelamar. Kedua file tersebut berfungsi untuk menampilkan menu pilihan admin dan pelamar yang memiliki privilege berbeda-beda. 

• Folder Controller berisi 3 file python, yaitu controlAccount, controlLoker, controlPelamar. Ketiga file tersebut memiliki fungsi yang berbeda-beda. ControlAccount berfungsi untuk mengontrol data admin atau pelamar saat login. ControlLoker berfungsi untuk mengontrol privilege dan aktivitas dari user Admin. ControlPelamar berfungsi untuk mengontrol privilege dan aktivitas dari user Pelamar. 

C. Main
Selain folder MVC, terdapat file Main yang berisi kode python untuk file utama yang menjalankan semua aktivitas program aplikasi Loker. 

D. Readme
Readme berisi penjelasan detail beserta dokumentasi mengenai program aplikasi Loker kelompok kami.
