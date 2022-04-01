#podstawowe podejście

# with open("dane.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

#wykorzystanie biblioteki csv
# import csv

# with open("dane.csv") as data_file:
#     data = csv.reader(data_file, delimiter=';')
#     mails = []
#     for row in data:
#         if row[1]!="name":
#             mails.append(row[2])
#     print(mails)

#wykorzystanie biblioteki pandas
#należy ją najpierw zaimportować
