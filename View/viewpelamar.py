from Controller import controlAccount
from Controller import controlPelamar
from Controller import controlLoker
import os, time

ll = controlPelamar.LinkedList()
lili = controlLoker.LinkedList()

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
            print("Loading...")
            time.sleep(5)
            os.system("cls")
        elif pilihadmin == '2':
            ll.applypelamar()
            print("Loading...")
            time.sleep(7)
            os.system("cls")
        elif pilihadmin == '3':
            ll.sortList()
            print("Loading...")
            time.sleep(5)
            os.system("cls")
        elif pilihadmin == '4':
            controlAccount.profilpelamar()
            print("Loading...")
            time.sleep(5)
            os.system("cls")
        elif pilihadmin == '5':
            print("Anda akan diarahkan ke menu login")
            print("Loading...")
            time.sleep(3)
            os.system('cls')
            controlAccount.login()
        else:
            print('Pilihan anda tidak tersedia')
            time.sleep(1)
            os.system("cls")