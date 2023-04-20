from Model import database
from View import viewadmin
from View import viewpelamar
import pwinput
import os, time

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