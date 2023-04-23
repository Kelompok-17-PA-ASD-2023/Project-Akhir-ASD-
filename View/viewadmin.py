from Controller import controlAccount
from Controller import controlLoker
import os, time

lili = controlLoker.LinkedList()

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