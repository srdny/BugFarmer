import csv


# try:
#   with open("nonexistent_file.txt", "r") as file:
#     data = file.read()
#     print(data)
# except FileNotFoundError:
#     print("The specified file does not exist.")

data = [
  ['Item', 'Quantity'],
  ['Mugs', 2],
  ['Hangers', 30],
  ['Shoes', 2]
]

try:
# Work with files here
    with open('404.csv', 'r') as file:
        csv_reader = csv.reader(file)
        #file.readline()

        for row in csv_reader:
            print(row)

except FileNotFoundError:
# Catch errors here
    print('Packing list file not found. Creating a new one.')
    with open('404.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)