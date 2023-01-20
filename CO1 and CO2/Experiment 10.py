# Experiment 10:
# A program to find the volume of a cone:

# Declaring a variable to which the user inputs the radius of the cone:
Rds = int(input("Enter the radius of the cone : "))

# Declaring a second variable to which the user inputs the height of the cone:
Hght = int(input("Enter the height of the cone : "))

# Calculation:
Vlum = 1 / 3 * 3.14 * Rds * Rds * Hght  # Volume of a cone= 1/3 * pi * radius^2 * height

# Printing the result:
print("The volume of cone = ", Vlum)
