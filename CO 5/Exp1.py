# To write data to a file and print it line by line as list
choice = 0
with open("Q1.txt", 'w') as fl:  # In write mode
    while choice != "Exit":  # Loop to write until exit statement is True
        ln = input("Enter the line: ")  # User input
        fl.write(ln)
        fl.write("\n")
        choice = input("Type Exit and Press Enter to end. Or press Enter to continue:\n")
        if choice == "Exit":
            break

fl = open("Q1.txt")  # Default as text mode and read mode
fl_rl = fl.readlines()  # readlines() to read all lines of text
print("\nThe list of lines in text:\n", fl_rl)

fl_rl = [i.strip() for i in fl_rl]  # List comprehension to strip \n from the end of each line
print("\nThe list of lines in text after stripping:\n", fl_rl)

fl.close()
