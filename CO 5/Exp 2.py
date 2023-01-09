# To copy all odd lines from a file and store it in a different file
input_file = open("Q1.txt")  # Open the file from which the data should be copied
output_file = open("Q2.txt", 'w')  # Open in file in write mode to which the data should be copied to
copy_data = input_file.readlines()
print("File contents are:")
print(copy_data)  # Print all data from the first file as a list due to readline

for i in range(0, len(copy_data)):
    if i % 2 == 0:  # If condition to copy only the odd lines
        output_file.write(copy_data[i])
    else:
        pass
output_file.close()  # To exit write mode

output_file = open("Q2.txt", 'r')  # Open new file in read mode
print("\nCopied lines are:")
print(output_file.read())  # Print all lines to show the result

input_file.close()
output_file.close()  # Close both opened files
