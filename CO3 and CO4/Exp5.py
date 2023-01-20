import csv
reader = csv.reader(open("Sample.csv"))
for row in reader:
    print(row)
