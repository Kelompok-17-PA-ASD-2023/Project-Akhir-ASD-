from Controller import controlAccount
from Controller import controlLoker
import os, time

linked_list = controlLoker.LinkedList()

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
            linked_list.display()
            print("Loading...")
            time.sleep(5)
            os.system("cls")
        elif pilihadmin == '2':
            linked_list.add_database()
            linked_list.display()
            print("Loading...")
            time.sleep(5)
            os.system("cls")
        elif pilihadmin == '3':
            linked_list.delete()
            linked_list.display()
            print("Loading...")
            time.sleep(5)
            os.system("cls")
        elif pilihadmin == '4':
            linked_list.lihatuser()
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