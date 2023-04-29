# Project Akhir ASD Kelompok 17
Anggota kelompok : 
- Vera Santi Wijaya (2209116007)
- Juventia Adelia Putri (2209116032)
- Lidia Aprilia Putri (2209116041)

## 📌Deskripsi Program
- Berikut adalah program project kelompok kami dengan tema lowongan pekerjaan. Tujuan dibuatnya program ini untuk mengelola informasi mengenai lowongan pekerjaan di suatu perusahaan yang meliputi posisi kerja, nama perusahaan, nominal gaji, domisili perusahaan, dan maksimal umur pelamar kerja. Program kami menggunakan database Mongodb untuk menyimpan data-data lowongan pekerjaan diatas. 

-  Pada program kami, terdapat 2 user dengan privilege yang berbeda. Pertama, user admin. Admin memiliki privilege untuk menampilkan seluruh data loker, menambahkan data loker, menghapus data loker, dan melihat seluruh user pelamar. Kedua, user pelamar. Pelamar memiliki privilege untuk melihat daftar data loker, mencari data loker, mengurutkan data loker berdasarkan gaji dari yang terbesar, dan data profil pelamar.

- Untuk struktur di database Mongodb pada program kami terdiri dari dua Collection yaitu "my_collection" dan "privilege_login". 

- Pada "my_collection", terdapat 6 Documents yang memiliki Fields "_id" sebagai Primary Key, "job", "perusahaan", "gaji", "email", "domisili", dan "umur". 

- Untuk Collection "privilege_login", terdapat 4 Documents dengan satu Document memiliki Fields "_id" sebagai Primary Key, "nama", "pass", dan "privilege". Untuk ketiga Documents lainnya memiliki Fields "_id" sebagai Primary Key, "nama", "pass", "email", "pendidikan", "jurusan", "privilege", "tahun", dan "lahir".

## 📌Struktur Project

 * [Folder Controller](https://github.com/Kelompok-17-PA-ASD-2023/Project-Akhir-ASD-/edit/main/README.md#dalam-folder-controller)
    * [File controlAccount](https://github.com/Kelompok-17-PA-ASD-2023/Project-Akhir-ASD-/edit/main/README.md#%EF%B8%8F-file-controlaccount)
    * [File controlLoker](https://github.com/Kelompok-17-PA-ASD-2023/Project-Akhir-ASD-/edit/main/README.md#%EF%B8%8F-file-controlloker)
    * [File controlPelamar](https://github.com/Kelompok-17-PA-ASD-2023/Project-Akhir-ASD-/edit/main/README.md#%EF%B8%8F-file-controlpelamar)
    
 * [Folder Model](https://github.com/Kelompok-17-PA-ASD-2023/Project-Akhir-ASD-/edit/main/README.md#folder-model)
    * [File database](https://github.com/Kelompok-17-PA-ASD-2023/Project-Akhir-ASD-/edit/main/README.md#-file-database)
    
 * [Folder View](https://github.com/Kelompok-17-PA-ASD-2023/Project-Akhir-ASD-/edit/main/README.md#folder-view)
    * [File viewadmin](https://github.com/Kelompok-17-PA-ASD-2023/Project-Akhir-ASD-/edit/main/README.md#-file-viewadmin)
    * [File viewpelamar](https://github.com/Kelompok-17-PA-ASD-2023/Project-Akhir-ASD-/edit/main/README.md#-file-viewpelamar)
    
 * [File Main](https://github.com/Kelompok-17-PA-ASD-2023/Project-Akhir-ASD-/edit/main/README.md#file-main)

#### Model View Controller atau yang dapat disingkat MVC adalah sebuah pola arsitektur dalam membuat sebuah aplikasi dengan cara memisahkan kode menjadi tiga bagian. Implementasi MVC pada Program Aplikasi Loker di Repository Github Pada program kami yang terdiri dari :

![Cuplikan layar 2023-04-27 012912](https://user-images.githubusercontent.com/122012870/234919368-b31fdda1-5ddc-4acb-9ee9-ac7e2181cf9c.png)

- ⚙️ Controller bagian yang bertugas untuk menghubungkan serta mengatur model dan view agar dapat saling terhubung.
Folder Controller berisi 3 file python, yaitu controlAccount, controlLoker, controlPelamar. Ketiga file tersebut memiliki fungsi yang berbeda-beda. ControlAccount berfungsi untuk mengontrol data admin atau pelamar saat login. ControlLoker berfungsi untuk mengontrol privilege dan aktivitas dari user Admin. ControlPelamar berfungsi untuk mengontrol privilege dan aktivitas dari user Pelamar.

- 📂 Model Bagian yang bertugas untuk menyiapkan, mengatur, memanipulasi, dan mengorganisasikan data yang ada di database.
Folder Model berisi file python untuk mengakses database Mongodb.

- 💻 View Bagian yang bertugas untuk menampilkan informasi dalam bentuk Graphical User Interface (GUI).
Folder View berisi 2 file python, yaitu viewadmin dan viewpelamar. Kedua file tersebut berfungsi untuk menampilkan menu pilihan admin dan pelamar yang memiliki privilege berbeda-beda.

- 🔗 Main.
Selain folder MVC, terdapat file Main yang berisi kode python untuk file utama yang menjalankan semua aktivitas program aplikasi Loker.

## 📌Fitur dan Fungsionalitas

### Folder Controller
![Cuplikan layar 2023-04-27 013252](https://user-images.githubusercontent.com/122012870/234656715-b3cd74fc-708f-480c-9340-c0355f9378ce.png)
### ⚙️ File ControlAccount
- Mengimport Module dan Library

Mengimport module berfungsi sebagai multi file yaitu agar dapat memanggil file lain di dalam satu module yang berbeda, pada file ini file lain yang dipanggil ialah file database dari folder Model dan file viewadmin serta file viewpelamar yang masing-masingnya berasal dari folder View

Mengimport library dimaksudkan untuk memanfaatkan fungsionalitas dalam library tersebut untuk kebutuhan tertentu, di dalam program ini library yang digunakan adalah library `pwinput` yang bertugas mengenkripsikan password yang diinput pengguna, kemudian library `os` yang bertugas untuk melakukan berbagai macam operasi yang terkait dengan sistem operasi, dan yang terakhir adalah library `time` yang bertugas untuk melakukan operasi yang berkaitan dengan waktu dan tanggal

```
from Model import database
from View import viewadmin
from View import viewpelamar
import pwinput
import os, time
```

- Function Login

Fungsi Login adalah program yang digunakan untuk menampilkan perintah terkait login sebelum masuk ke dalam aplikasi, di dalamnya terdapat percabangan(if, elif, else) yang digunakan untuk mengeksekusi kode tertentu hanya jika kondisi tersebut terpenuhi. 

Di dalam penginputan juga terdapat metode bawaan python diantara adalah `lower` yang merupakan metode untuk mengubah seluruh karakter menjadi huruf kecil dan `capitalize` yang merupakan metode untuk mengubah karakter pertama dalam string menjadi huruf kapital sedangkan karakter lainnya adalah huruf kecil.

Untuk mencari nama yang sesuai dalam database maka diperlukan `find_one`, find_one sendiri ialah salah satu metode dalam Mongodb yang selanjutnya hasil pencarian tersebut akan tersimpan dalam variabel result 

Penggunaan statement `try except` dimaksudkan untuk menangani kesalahan penginputan data dari user yang tidak disengaja agar tidak terjadi error di dalam output program nantinya

```
def login():
    print('''\nSELAMAT DATANG! 
    > > > >....APLIKASI PENYEDIA LOWONGAN KERJA ONLINE....< < < <''')
    global penggunaLogin
    try:
        nama = str.lower(input("\nMasukkan username anda : "))
        user = nama.capitalize()
        pw = str(pwinput.pwinput("Masukkan password anda : "))
        result = database.role.find_one({"nama": user, })
        penggunaLogin = user

        if result is None:
            print("MOHON PERIKSA USERNAME DAN PASSWORD ANDA KEMBALI!")
            time.sleep(2)
            os.system('cls')
            login()

        elif result['nama'] == user and pw== result['pass']:
            print("Berhasil Login")
            if result["privilege"] == "admin":
                os.system('cls')
                print("SELAMAT DATANG", user)
                os.system('cls')
                viewadmin.menuAdmin()

            elif result["privilege"] == "pelamar":
                os.system('cls')
                print("SELAMAT DATANG", user)
                viewpelamar.menuPelamar()
        else:
            print("MOHON PERIKSA USERNAME DAN PASSWORD ANDA KEMBALI!")
            time.sleep(2)
            os.system('cls')
            login()
    except KeyboardInterrupt:
            print("\nMAAF PROGRAM TIDAK MENGERTI!")
            time.sleep(2)
            os.system('cls')
            login()
```

- Function profilpelamar

Function profilpelamar adalah program yang menampilkan perintah terkait dengan data-data si pelamar yang telah tersimpan dalam database, menggunakan metode `find_one` untuk mencari data sesuai nama pelamar yang sedang login

```
def profilpelamar():
    pelamar = database.role.find_one({"nama": penggunaLogin})
    print("\n-------------- PROFIL PELAMAR --------------")
    print("> Nama Pelamar     :", pelamar["nama"])
    print("> Tanggal Lahir    :", pelamar["lahir"]) 
    print("> Email Pelamar    :", pelamar["email"])
    print("> Pendidikan       :", pelamar["pendidikan"])
    print("> Jurusan          :", pelamar["jurusan"]) 
    print("> Tahun Bergabung  :", pelamar["tahun"]) 
    print("> Sebagai          :", pelamar["privilege"])
    print("--------------------------------------------")
```

### ⚙️ File ControlLoker
- Mengimport Module dan Library

Mengimport module berfungsi sebagai multi file yaitu agar dapat memanggil file lain di dalam satu module yang berbeda, pada file ini file lain yang dipanggil ialah file database dari folder Model 

Mengimport library dimaksudkan untuk memanfaatkan fungsionalitas dalam library tersebut untuk kebutuhan tertentu, di dalam program ini library yang digunakan adalah library `prettytable` yang bertugas untuk menyusun data ke dalam tabel-tabel agar terlihat rapi dan mudah dibaca, serta ada library `os` yang bertugas untuk melakukan berbagai macam operasi yang terkait dengan sistem operasi.

```
from Model import database
from prettytable import PrettyTable
import os
```

- Class Node

Class Node adalah untuk mempresentasikan sebuah simpul dalam Linked list

```
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
```

- Class LinkedList

Class LinkedList adalah salah satu struktur data yang yang terdiri dari node-node yang terhubung satu sama lain. Dalam Class LinkedList, fungsi def init dan self berperan sebagai konstruktor untuk membuat instance dari class tersebut

Nantinya setiap method dalam linked list akan memiliki parameter self. Dengan menggunakan parameter `self` kita dapat mengakses atribut-atribut yang ada pada Class LinkedList

```
class LinkedList:
    def __init__(self):
        self.head = None
```

- Method append

Method ini berfungsi untuk menambahkan node baru di bagian akhir linked list. Method kemudian akan membuat istance baru dari class Node dan menyimpan data pada node tersebut.

```
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
```

- Method add_data

Method ini berfungsi untuk menambahkan data yang sesuai dengan penempatannya dengan database ke dalam method append. 

```
    def add_data (self):
        tambah = database.mycol.find()
        for i in tambah:
            job = i["job"]
            perusahaan = i["perusahaan"]
            gaji = i["gaji"]
            email = i["email"]
            domisili = i["domisili"]
            umur = i["umur"]

            data = [job, perusahaan, gaji, email, domisili, umur] 

            self.append(data)
```

- Method add_database

Method ini berfungsi untuk memasukkan inputan dari user ke dalam database menggunakan salah satu metode mongodb yaitu metode `insert_one`

Terdapat pengkondisian yang melibatkan metode `isspace` python yang berfungsi untuk mencegah inputan kosong masuk ke dalam database

```
    def add_database(self):
        while True:
            try:     
                job = str.lower(input("Posisi Job            : "))
                perusahaan = str.lower(input("Nama Perusahaan       : "))
                gaji = int(input("Nominal Gaji          : "))
                email = str.lower(input("Email Perusahaan      : "))
                domisili = str.lower(input("Domisili              : "))
                umur = int(input("Maksimal Umur Pekerja : "))

                if job.isspace() or perusahaan.isspace() or email.isspace() or domisili.isspace() or not job or not perusahaan or not email or not domisili:
                    print("\nMOHON JANGAN KOSONGKAN DATA!")
                else:
                    data = {"job" : job,
                            "perusahaan" : perusahaan,
                            "gaji" : gaji,
                            "email": email,
                            "domisili": domisili,
                            "umur" : umur}
                    database.mycol.insert_one(data).inserted_id
                    print("\nData berhasil ditambahkan")
                    break

            except ValueError:
                print("\nMOHON ISI SESUAI KETENTUAN!\n")
            except KeyboardInterrupt:
                print("\n\nMAAF PROGRAM TIDAK MENGERTI!\n")
```

- Method display
Method ini berfungsi untuk menampilkan seluruh data-data yang berada di dalam database yang kemudian tersusun di dalam table berkat bantuan dari library `prettytable`. 

```
    def display(self):
        data = []
        for i in database.mycol.find({}):
            data.append(i)

        if not data:
            print("MAAF LOKER KOSONG")
        else:
            table = PrettyTable(['Bagian Posisi', 'Nama Perusahaan', 'Nominal Gaji', "Email Perusahaan", "Domisili Perusahaan", "Maksimal Umur"])
            for x in data:
                table.add_row([x['job'], x['perusahaan'], x['gaji'], x['email'], x['domisili'], x['umur']])
            print(table)
```

- Method search
Method ini berfungsi untuk mencari suatu data dalam database menggunakan jenis pencarian `jump search`. Algoritma jump menggunakan teknik loncatan untuk melakukan pencarian secara efisien.

```
    def search(self, temp, key):
        temp = []
        for i in database.mycol.find({}):
            temp.append(i)

        if not temp:
            print("MAAF LOKER KOSONG")
            return

        n = len(temp)
        step = int(n ** 0.5)
        prev = 0
        while prev < n and temp[prev]['job'] < key:
            prev += step
        prev -= step
        while prev < n:
            if temp[prev]['job'] == key:
                return (temp[prev])
            prev += 1
        return None
```

- Method delete
Method ini berfungsi untuk menghapus suatu data dari dalam database dengan memanfaatkan teknik pencarian jump dari method search yang kemudian akan di hapus dari dalam database menggunakan perintah `delete_one`

```
    def delete(self):
        while True:
            try:
                self.display()
                temp = []
                for i in database.mycol.find({}):
                    temp.append(i)

                key = str.lower(input("pilih Loker: "))
                result = self.search(temp , key) 

                if result:
                    database.mycol.delete_one({"job": key})
                    print("\nLOKER BERHASIL DIHAPUS!")
                elif not result:
                    print("\nLOKER TIDAK DITEMUKAN!")
                else:
                    print("\nLOKER TIDAK DITEMUKAN!")
                break

            except ValueError:
                    print("\nMOHON ISI SESUAI KETENTUAN!")
            except KeyboardInterrupt:
                    print("\n\nMAAF PROGRAM TIDAK MENGERTI!")
```

- Method lihatuser
Method ini berfungsi untuk menampilkan seluruh user dari dalam database yang kemudian disusun kedalam sebuah table

```
    def lihatuser(self):
        datauser = []            
        for i in database.role.find({}):
            datauser.append(i)

        if not datauser:
            print("MAAF PENGGUNA TIDAK ADA")
        else:
            table = PrettyTable(['Nama', 'Sebagai'])
            for x in datauser:
                table.add_row([x['nama'], x['privilege']])
            print(table)
```

- Method load

Method ini berfungsi untuk menampilkan perintah inputan enter yang harus diisi user yang bertujuan untuk memisahkan antara menu utama dan hasil kerja dari method-method diatas di output nantinya 

```
    def load(self):
        ask = input("\nTekan Enter Untuk Lanjut ...")
        if ask == "":
            os.system("cls")
        else:
            os.system("cls")
```

### ⚙️ File ControlPelamar
- Mengimport Module dan Library

Mengimport module berfungsi sebagai multi file yaitu agar dapat memanggil file lain di dalam satu module yang berbeda, pada file ini file lain yang dipanggil ialah file database dari folder Model 

Mengimport library dimaksudkan untuk memanfaatkan fungsionalitas dalam library tersebut untuk kebutuhan tertentu, di dalam program ini library yang digunakan adalah library `prettytable` yang bertugas untuk menyusun data ke dalam tabel-tabel agar terlihat rapi dan mudah dibaca, serta ada library `os` yang bertugas untuk melakukan berbagai macam operasi yang terkait dengan sistem operasi.

```
from Model import database
from prettytable import PrettyTable
import os
```

- Class Node

Class Node adalah untuk mempresentasikan sebuah simpul dalam Linked list

```
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
```

- Class LinkedList

Class LinkedList adalah salah satu struktur data yang yang terdiri dari node-node yang terhubung satu sama lain. Dalam Class LinkedList, fungsi def init dan self berperan sebagai konstruktor untuk membuat instance dari class tersebut

Nantinya setiap method dalam linked list akan memiliki parameter self. Dengan menggunakan parameter `self` kita dapat mengakses atribut-atribut yang ada pada Class LinkedList

```
class LinkedList:
    def __init__(self):
        self.head = None
```

- Method mergeSort

Method ini berfungsi untuk mengurutkan suatu nilai di dalam database, di dalam program ini nilai yang diurutkan adalah gaji. teknik sorting yang digunakan adalah `merge sort` yaitu teknik sorting yang algoritmanya membagi 2 array secara rekursif yang kemudian memasukkankan kembali ke dalam satu array yang terurut

```
    def mergeSort(self, data):
            temp = []
            for i in database.mycol.find({}):
                temp.append(i)

            if not temp:
                print("MAAF LOKER KOSONG")
                return
            
            if len(data) > 1:
                mid = len(data) // 2
                left = data[:mid]
                right = data[mid:]

                self.mergeSort(left)
                self.mergeSort(right)

                i = j = k = 0
                while i < len(left) and j < len(right):
                    if left[i]["gaji"] > right[j]["gaji"]:
                        data[k] = left[i]
                        i += 1
                    else:
                        data[k] = right[j]
                        j += 1
                    k += 1

                while i < len(left):
                    data[k] = left[i]
                    i += 1
                    k += 1

                while j < len(right):
                    data[k] = right[j]
                    j += 1
                    k += 1
            return data
```

- Method sortList

Method ini berfungsi menampilkan hasil dari method mergeSort yang kemudian hasilnya disimpan dalam variable result 

```
    def sortList(self):
        temp = []
        for i in database.mycol.find({}):
            temp.append(i)

        if not temp:
            print("MAAF LOKER KOSONG")
            return

        result = self.mergeSort(temp) 

        print("\nMENGURUTKAN GAJI DARI NOMINAL TERBESAR!")
        table = PrettyTable(['Bagian Posisi', 'Nama Perusahaan', 'Nominal Gaji', "Email Perusahaan", "Domisili Perusahaan", "Maksimal Umur"])
        for x in result:
            table.add_row([x['job'], x['perusahaan'], x['gaji'], x['email'], x['domisili'], x['umur']])
        print(table)
```

- Method jumpsearch
Method ini berfungsi untuk mencari suatu nilai nama job yang terdapat di database menggunakan jenis pencarian `jump search`. Algoritma jump search menggunakan teknik jump atau loncatan untuk melakukan pencarian secara efisien

```
    def jumpsearch(self, temp, key):
        temp = []
        for i in database.mycol.find({}):
            temp.append(i)

        if not temp:
            print("MAAF LOKER KOSONG")
            return

        n = len(temp)
        step = int(n ** 0.5)
        prev = 0
        while prev < n and temp[prev]['job'] < key:
            prev += step
        prev -= step
        while prev < n:
            if temp[prev]['job'] == key:
                return (temp[prev])
            prev += 1
        return None
```

- Method applypelamar

Method ini berfungsi untuk menampilkan hasil pencarian dari method jumpsearch yang kemudian hasilnya akan tersimpan dalam variable result, hasil dari variable result itu kemudian akan diappend ke dalam list kosong agar nantinya data dapat ditampilkan dalam prettytable. Ketika pengkondisian menyatakan menemukan nilai yang dicari dalam suatu database maka selanjutnya akan tertampil printan berupa persyaratan loker

```
    def applypelamar(self):
        temp = []
        col = []
        for i in database.mycol.find({}):
            temp.append(i)
        while True:
            try:
                key = str.lower(input("Ingin mendaftar posisi apa: "))
                result = self.jumpsearch(temp , key) 
                col.append(result) 

                if result is None:
                    print("maaf tidak ditemukan")
                else:
                    table = PrettyTable(['Bagian Posisi', 'Nama Perusahaan', 'Nominal Gaji', "Email Perusahaan", "Domisili Perusahaan", "Maksimal Umur"])
                    for x in col:
                        table.add_row([x['job'], x['perusahaan'], x['gaji'], x['email'], x['domisili'], x['umur']])
                    print(table)
                    print('Adapun persyaratan', key, '''yang diperlukan yaitu:
                    1. Cover Letter
                    2. CV
                    3. Portofolio
                    4. Ijazah dan transkrip nilai
                    5. Sertifikat dan piagam penghargaan
                    6. Pas foto terbaru
                    7. Fotokopi Identitas terbaru
                    8. SKCK 
                    ''')
                break
                   
            except ValueError:
                    print("\nMOHON ISI SESUAI KETENTUAN!")
            except KeyboardInterrupt:
                    print("\n\nMAAF PROGRAM TIDAK MENGERTI!")
```

- Method loading

Method ini berfungsi untuk menampilkan perintah inputan enter yang harus diisi user yang bertujuan untuk memisahkan antara menu utama dan hasil kerja dari method-method diatas di output nantinya 

```
    def loading(self):
        ask = input("\nTekan Enter Untuk Lanjut ...")
        if ask == "":
            os.system("cls")
        else:
            os.system("cls")
```         


### Folder Model
![image](https://user-images.githubusercontent.com/122012870/234690947-03aa5e08-a588-49f9-aee3-b8043f63aebe.png)
### 📂 File database
- import module 
Dengan mengimport `pymongo`, kita dapat menggunakan semua fungsionalitas yang disediakan oleh library ini. Dan dengan mengimport `MongoClient`, kita dapat membuat koneksi ke server MongoDB dan mengakses database dan koleksi yang ada di dalamnya

```
from pymongo import MongoClient
```
- Memasukkan URI MongoDB didalam nama variable client dengan bantuan `MongoClient` agar dapat membuat koneksi dan mengakses database didalamnya

```
client = MongoClient('mongodb+srv://verasantiwijayaa:s3WNDPpdhS3g7xIX@cluster0.yuyn0jm.mongodb.net/test')
```
- Membuat koleksi "my_collection" dan koleksi "Privilege_Login" di dalam database "Nama_Database" di masing-masing variable yang berbeda

```
mydb = client["Nama_Database"]
mycol = mydb["my_collection"]
role = mydb["Privilege_Login"]
```

- Database MongoDb untuk koleksi "my_collection"

![image](https://user-images.githubusercontent.com/122012870/234924287-1b604555-f7c8-4b70-9a81-317b65678767.png)

- Database MongoDb untuk koleksi "Privilege_Login"

![image](https://user-images.githubusercontent.com/122012870/234925312-1bd449bc-1f0e-4ad8-b8d0-ff2fa3ccd616.png)

### Folder View
![image](https://user-images.githubusercontent.com/122012870/234727047-608e4222-ed2f-4a42-8f0b-4271c0e700fe.png)

### 💻 File viewadmin
- Mengimport Module dan Library

Mengimport module berfungsi sebagai multi file yaitu agar dapat memanggil file lain di dalam satu module yang berbeda, pada file ini, file lain yang dipanggil ialah file controlAccount serta file controlLoker yang masing-masingnya berasal dari folder Controller

Mengimport library dimaksudkan untuk memanfaatkan fungsionalitas dalam library tersebut untuk kebutuhan tertentu, di dalam program ini library yang digunakan adalah library `os` yang bertugas untuk melakukan berbagai macam operasi yang terkait dengan sistem operasi dan library `time` yang bertugas untuk melakukan operasi yang berkaitan dengan waktu dan tanggal

```
from Controller import controlAccount
from Controller import controlLoker
import os, time
```

- pemanggilan class linked list 

Untuk pemanggilan class LinkedList di dalam file controlLoker yang dideklarasikan dalam variable bernama lili, pemanggilan ini berfungsi agar method-method yang ada di dalam class LinkedList dapat berjalan ketika ingin digunakan

```
lili = controlLoker.LinkedList()
```

- Function menuAdmin

function ini berfungsi untuk menampilkan menu yang dimiliki oleh privilege admin, yang di dalamnya terdapat looping `while True` agar menu dapat terus berjalan secara berulang-ulang. Selain itu, di dalamnya function ini terdapat bercabangan(if-elif-else) yang dimana setiap pengkodisian yang berbeda akan menampilkan menu yang berbeda sesuai dengan pilihan yang diinput pengguna yang nantinya menu akan berhubungan langsung dengan method-method yang ada di dalam Class LinkedList dan function dalam file controlAccount

```
def menuAdmin():
    while True:
        print("Selamat Datang Admin")
        pilihadmin = str(input('''
        ==============================
        |         MENU  ADMIN        |
        ==============================
        |-----Menu yang tersedia-----|
        |                            |
        |  1. Display Seluruh Data   |
        |  2. Tambahkan Data Loker   |
        |  3. Hapus Data Loker       |
        |  4. Lihat Seluruh User     |
        |  5. Sign Out               |
        |                            |
        ==============================

    Masukkan Pilihan (1/2/3/4/5): '''))

        if pilihadmin == '1':
            lili.display()
            lili.load()
        elif pilihadmin == '2':
            lili.add_database()
            lili.display()
            lili.load()
        elif pilihadmin == '3':
            lili.delete()
            lili.display()
            lili.load()
        elif pilihadmin == '4':
            lili.lihatuser()
            lili.load()
        elif pilihadmin == '5':
            print("Anda akan diarahkan ke menu login")
            lili.load()
            controlAccount.login()
        else:
            print('Pilihan anda tidak tersedia')
            time.sleep(1)
            os.system("cls")
```
### 💻 File viewpelamar
- Mengimport Module dan Library

Mengimport module berfungsi sebagai multi file yaitu agar dapat memanggil file lain di dalam satu module yang berbeda, pada file ini, file lain yang dipanggil ialah file controlAccount, file controlLoker, serta file controlPelamar yang ketiga-tiganya berasal dari folder Controller

Mengimport library dimaksudkan untuk memanfaatkan fungsionalitas dalam library tersebut untuk kebutuhan tertentu, di dalam program ini library yang digunakan adalah library `os` yang bertugas untuk melakukan berbagai macam operasi yang terkait dengan sistem operasi dan library `time` yang bertugas untuk melakukan operasi yang berkaitan dengan waktu dan tanggal

```
from Controller import controlAccount
from Controller import controlPelamar
from Controller import controlLoker
import os, time
```

- pemanggilan class linked list 

Untuk pemanggilan class LinkedList di dalam file controlLoker yang dideklarasikan dalam variable bernama lili, sedangkan untuk pemanggilan Class LinkedList di dalam file controlPelamar dideklarasikan dalam variable bernama ll. Pemanggilan ini berfungsi agar method-method yang ada di dalam class LinkedList dapat berjalan ketika digunakan

```
ll = controlPelamar.LinkedList()
lili = controlLoker.LinkedList()
```

- Function menuPelamar

function ini berfungsi untuk menampilkan menu yang dimiliki oleh privilege pelamar, yang di dalamnya terdapat looping `while True` agar menu dapat terus berjalan secara berulang-ulang. Selain itu, di dalam function ini terdapat bercabangan(if-elif-else) yang dimana setiap pengkodisian yang berbeda akan menampilkan menu yang berbeda pula sesuai dengan pilihan yang diinput pengguna yang nantinya menu tersebut akan berhubungan langsung dengan method-method yang ada di dalam Class LinkedList baik dalam file controlPelamar maupun file controlLoker serta function-function dari dalam file controlAccount

```
def menuPelamar():
    while True:
        print("Percayakan Loker Pada Kami!")
        pilihadmin = str(input('''
        ==============================
        |        MENU PELAMAR        |
        ==============================
        |-----Menu yang tersedia-----|
        |                            |
        |  1. Lihat Daftar Loker     |
        |  2. Cari dan Daftar Loker  |
        |  3. Urutkan Gaji Loker     |
        |  4. Profil Pelamar         |
        |  5. Sign Out               |
        |                            |
        ==============================

    Masukkan Pilihan (1/2/3/4/5): '''))

        if pilihadmin == '1':
            lili.display()
            ll.loading()
        elif pilihadmin == '2':
            ll.applypelamar()
            ll.loading()
        elif pilihadmin == '3':
            ll.sortList()
            ll.loading()
        elif pilihadmin == '4':
            controlAccount.profilpelamar()
            ll.loading()
        elif pilihadmin == '5':
            print("Anda akan diarahkan ke menu login")
            ll.loading()
            controlAccount.login()
        else:
            print('Pilihan anda tidak tersedia')
            time.sleep(1)
            os.system("cls")
```

### File Main
![image](https://user-images.githubusercontent.com/122012870/234732578-ba051bef-5e65-412f-ae11-f13565ed4b68.png)

- Import modul

Mengimport module berfungsi sebagai multi file yaitu agar dapat memanggil file lain di dalam satu module yang berbeda, pada file ini, file lain yang dipanggil ialah file controlAccount yang berasal dari folder Controller yang diberikan nama alternatif atau nama alias pada modul controlAccount sebagai `c`

```
from Controller import controlAccount as c
```

- if __name__ == __main__:

`if __name__ == "__main__"` pada Python memungkinkan kita untuk menentukan baris tertentu manakah yang akan dijalankan ketika script berbentuk file kita jalankan. pada program berikut baris pertama yang akan di running terlebih dahulu ialah function login pada file controlAccount di dalam folder Controller

```
if __name__ == "__main__":
    c.login()
```

## 📌Cara Penggunaan

📍Ketika user pertama kali masuk ke dalam aplikasi LOKER, User akan dihadapkan pada halaman awal login, di halaman ini User diharuskan untuk mengisi username dan password.

![image](https://user-images.githubusercontent.com/122012870/235292171-78fbc48f-a088-4960-8101-97238076bcd8.png)

📍Ketika username dan password yang dimiliki Admin dinyatakan benar oleh program, maka selanjutnya halaman yang berisikan menu-menu yang hanya dapat diakses oleh Admin akan tertampil di dalam aplikasi LOKER

![Cuplikan layar 2023-04-29 161358](https://user-images.githubusercontent.com/122012870/235292433-1a88a2c7-1d2c-41cc-912d-639c5a0cab69.png)

📍Di halaman menu, Admin diminta untuk memilih opsi nomor menu sesuai dengan keinginan dan kebutuhan Admin

![image](https://user-images.githubusercontent.com/122012870/235292407-752b1630-ff9e-44f5-aa84-8bfa40378873.png)

📍Ketika Admin memilih menu Display Seluruh Data pada nomor menu 1, maka kemudian program akan menampilkan tabel yang berisikan data-data lowongan pekerjaan yang telah tersimpan dalam server database sebelumnya, seperti hal nya bagian posisi job, nama perusahaan, nominal gaji, email perusahaan, domisili perusahaan, dan umur maksimal pekerja

![image](https://user-images.githubusercontent.com/122012870/235292517-f1823d1e-c84b-4c6c-8988-9807fc8b4a50.png)

📍 Ketika Admin memilih menu Tambahkan Data Loker pada nomor menu 2, maka kemudian program akan mengharuskan Admin untuk mengisi keseluruhan data-data baru  yang berkaitan dengan lowongan pekerjaan, seperti halnya posisi job, nama perusahaan, nominal gaji, email perusahaan, domisili perusahaan, dan maksimal umur pekerja. Data berikut harus diisi secara lengkap tanpa ada  pengosongan penginputan dan pengisian data harus sesuai arahan

![image](https://user-images.githubusercontent.com/122012870/235292827-a80a392b-d0db-4612-8f6d-ef08fb986482.png)

📍Ketika admin memilih menu Hapus Data Loker pada nomor menu 3, maka kemudian program akan meminta Admin untuk menginput nama posisi job yang ingin dihapus, jika nama posisi job yang tersimpan dalam database sesuai dengan inputan Admin maka seluruh data dari posisi job tersebut akan terhapus dari dalam aplikasi maupun dari dalam penyimpanan database

![image](https://user-images.githubusercontent.com/122012870/235293230-7c5bcf6c-7b8c-4f22-a484-949de7396fc4.png)

📍Ketika admin memilih menu Lihat Seluruh User pada nomor menu 4, maka kemudian program akan menampilkan tabel yang berisikan sejumlah user lain di dalam aplikasi LOKER tersebut

![image](https://user-images.githubusercontent.com/122012870/235293322-b234b30e-b3c5-43c0-8f2f-e74af42d7d29.png)

📍Ketika admin memilih menu Sign Out pada nomor menu 5, program akan kembali ke halaman awal aplikasi yaitu halaman login User

![Cuplikan layar 2023-04-29 163340](https://user-images.githubusercontent.com/122012870/235293369-cf06ed2f-5777-4a9f-864d-88324eb518de.png)

![image](https://user-images.githubusercontent.com/122012870/235293374-e054b40e-fd30-412c-9434-3d4ef26df4a6.png)

📍Namun ketika Admin salah menginputkan nomor menu maka program akan memastikan lagi untuk meminta nomor menu kembali hingga nomor menu tersebut dinyatakan sesuai dengan nomor menu yang ada di dalam aplikasi LOKER

![image](https://user-images.githubusercontent.com/122012870/235293538-1e4ab401-4768-40f4-ae3a-523c2622f038.png)

##### USER PELAMAR

👩‍💻Ketika username dan password yang dimiliki oleh salah satu Pelamar dinyatakan benar oleh program, maka selanjutnya halaman yang berisikan menu-menu yang hanya dapat diakses oleh Pelamar akan tertampil di dalam aplikasi LOKER

![Cuplikan layar 2023-04-29 163510](https://user-images.githubusercontent.com/122012870/235293458-68bea963-c90d-40cc-a947-09713b4236d5.png)

👩‍💻Di halaman menu, Pelamar diminta untuk memilih opsi nomor menu yang sesuai dengan keinginan dan kebutuhan si Pelamar

![image](https://user-images.githubusercontent.com/122012870/235293583-8ed84080-524a-4c7e-a95e-a9902f029cb2.png)

👩‍💻Jika Pelamar ingin melihat seluruh data-data mengenai lowongan pekerjaan yang telah tersedia dalam aplikasi LOKER, Pelamar dapat memilih nomor menu 1. Pada pilihan menu ini, Pelamar akan melihat tampilan tabel-tabel yang berisikan seluruh informasi terkait lowongan pekerjaan tersebut seperti halnya bagian posisi job, nama perusahaan, nominal gaji, email perusahaan, domisili perusahaan, dan umur maksimal pekerja

![image](https://user-images.githubusercontent.com/122012870/235293795-4896a4bb-ce22-415d-a07c-b95a85e49289.png)

👩‍💻Jika Pelamar ingin mencari dan mendaftar pekerjaan, Pelamar dapat memilih nomor menu 2. Pada pilihan menu ini Pelamar akan diminta untuk menginputkan nama posisi job yang ingin dicari, ketika nama posisi job ditemukan dalam server database LOKER, program akan menampilkan seluruh data-data yang terkait posisi job itu disertai dengan syarat-syarat untuk mendaftar pekerjaan tersebut

![image](https://user-images.githubusercontent.com/122012870/235293951-04685ee3-6d2a-4465-93d0-7af66c4b2eab.png)

👩‍💻Jika Pelamar ingin melihat seluruh posisi job dimulai dengan gaji job yang paling tertinggi, Pelamar dapat memilih nomor menu 3. Pada pilihan menu ini Pelamar akan melihat tampilan keseluruhan informasi lowongan pekerjaan yang diawali dengan posisi job yang teratas dengan nominal gaji tertinggi hingga pada job dengan nominal gaji terendah yang berada di dalam aplikasi LOKER

![image](https://user-images.githubusercontent.com/122012870/235294122-367efc3f-c6fa-4237-9621-8018aa70e697.png)
