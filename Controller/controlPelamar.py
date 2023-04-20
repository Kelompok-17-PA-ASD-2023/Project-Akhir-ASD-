from Model import database
from prettytable import PrettyTable

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def mergeSort(self, data):
            temp = []
            for i in database.mycol.find({}):
                temp.append(i)

            if not temp:
                print("List masih kosong")
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
        
    def sortList(self):
        temp = []
        for i in database.mycol.find({}):
            temp.append(i)

        if not temp:
            print("List masih kosong")
            return

        result = self.mergeSort(temp) 

        print("\nMENGURUTKAN GAJI DARI NOMINAL TERBESAR!")
        table = PrettyTable(['Bagian Posisi', 'Nama Perusahaan', 'Nominal Gaji', "Email Perusahaan", "Domisili Perusahaan", "Maksimal Umur"])
        for x in result:
            table.add_row([x['job'], x['perusahaan'], x['gaji'], x['email'], x['domisili'], x['umur']])
        print(table)
