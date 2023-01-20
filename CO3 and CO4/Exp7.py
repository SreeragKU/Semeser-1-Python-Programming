import csv
csv_string = """a,b,c
d,e,f
g,h,i"""
print("Original string:")
print(csv_string)
lines = csv_string.splitlines()
print("List of CSV formatted strings:")
print(lines)
reader = csv.reader(lines)
parsed_csv = list(reader)
print("\nList representation of the CSV file:")
print(parsed_csv)
