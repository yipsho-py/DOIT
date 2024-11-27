####### დავალება 1 ######
import csv 
new_list=[ ]
with open('titanic.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    headers = next(reader)
    name_index = headers.index("Survived")
    for row in reader:
        if row[name_index] == '1':        
            new_list.append(row)

import csv
with open('survived.csv', 'w',  encoding='utf-8') as file:
    writer = csv.writer(file)
    for item in new_list:
        writer.writerows(new_list)

# print(new_list)

####### დავალება 2 ######


import csv
new_list=[]
with open('organizations-100.csv', 'r', encoding= 'utf-8') as csv_file:
    reader = csv.reader(csv_file)
    headers = next(reader)
    name_index = headers.index('Number of employees')
    for row in reader:
        new_list.append(row)
 