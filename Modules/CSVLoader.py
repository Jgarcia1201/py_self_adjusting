from Model.Package import Package
from Model.HashTable import ChainingHashTable

import csv


def load_package_data():
    # Opening CSV File.
    with open("./CSV/PackageFileClean.csv", encoding='utf-8-sig') as csv_file:
        package_data = csv.reader(csv_file, delimiter=",")
        hashtable = ChainingHashTable(package_data.__sizeof__())  # Creating Hashtable to Return
        # Reading Data From Rows
        for row in package_data:
            package_id = int(row[0].strip())
            deliv = row[1].strip()
            city = row[2].strip()
            state = row[3].strip()
            zip = row[4].strip()
            deadline = row[5].strip()
            weight = row[6].strip()
            notes = row[7].strip()

            # Conversion
            key = int(package_id)

            # Creating Temporary Package Object & Inserting Into Hashtable
            temp = Package(package_id, deliv, city, state, zip, deadline, weight, notes)
            hashtable.insert(key, temp)
    return hashtable


def load_distance_data():
    distance_list = []
    with open("./CSV/DistanceTable.csv", encoding='utf-8-sig') as csv_file:
        distance_data = csv.reader(csv_file, delimiter=',')
        for row in distance_data:
            for i in range(len(row)):
                if row[i] == '':
                    continue
                else:
                    row[i] = float(row[i])
            row_list = list(row)
            distance_list.append(row_list)
    return distance_list


def load_address_data():
    address_book = {}
    id_gen = 0
    with open("./CSV/AddressData.csv", encoding="utf-8-sig") as csv_file:
        address_data = csv.reader(csv_file, delimiter=',')
        for row in address_data:
            address = row[1]
            address_book.__setitem__(address, id_gen)
            id_gen += 1
    return address_book
