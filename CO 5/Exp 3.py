# Read each row of a csv file and print as list of strings
import csv

with open("sr.csv", 'r') as file:  # opening the required csv file
    reader = csv.reader(file)  # Create a csv reader and reading the csv file

    for row in reader:
        print(row)  # Print each row of csv file as list of stings
