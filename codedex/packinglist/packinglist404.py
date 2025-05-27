import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

try:
    with open('packinglist.csv','r',encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)

except FileNotFoundError:
    print("data doesn't exist, add a new one")
    with open('packinglist.csv','w',newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)