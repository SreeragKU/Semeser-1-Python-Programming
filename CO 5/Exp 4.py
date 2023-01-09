# To print specific columns of the csv file
import csv

columns_to_read = [0,2]
with open("sr.csv", 'r') as file:  # opening the required csv file
    reader = csv.reader(file)  # Create a csv reader and reading the csv file

    for row in reader:
        print([row[i] for i in columns_to_read])  # Print each row of csv file as list of stings

