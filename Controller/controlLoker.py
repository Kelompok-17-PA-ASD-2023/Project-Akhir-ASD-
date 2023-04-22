from Model import database
from prettytable import PrettyTable
import time

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
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
    
    def load(self):
        count = 0

        for t in range(101):
            time.sleep(0.05)
            print(f'\rLoading.. |{t}%|', end='', flush=True)
            count += 1
            if count == 3:
                count = 0