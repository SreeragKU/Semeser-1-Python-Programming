import csv
reader = csv.reader(open("Sample.csv"))
no_lines= len(list(reader))
print("Number of lines in the given csv: ")
print(no_lines)
