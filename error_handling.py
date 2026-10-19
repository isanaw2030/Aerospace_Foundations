# Error Handling and Programs Safety
# Teaching Programs to survive problems


# try and except block

try :
    number = int(input("Enter a number : ")) # This executes only if a valid number entered
    print(number)

except :
    print("Invalid number. Please use numerical values only") # This executes if invalid number entered instead of program crashing badly


# handling missing files when opened in read mode

try :
    with open("data.txt", "r") as file:
        print(file.read())

except :
    print("File not found")


# Handling impossible calculation - zero division error

try :
    a = 10
    b = 0
    results = a / b
    print(results)

except :
    print("Impossible calculations attempted, division by zero!")

# else block

try :
    number = int(input("Enter a number : "))

except :
    print("Invalid input, please use numerical values only") # Executes only if invalid input entered

else :
    print("Conversion successful.") # executes only if valid input is entered


# Finally block - always executes!

try :
    print("Mission Starts")

except :
    print("Warning detected")

finally :
    print("System shutting down")

# catching specific error

try :
    number = int(input("Enter a number : "))
    print(number)

except ValueError :
    print("Please use numerical values only")


try :
    with open("data.txt", "r") as file:
        print(file.read())

except FileNotFoundError :
    print("Corrupted or Missing File!")


try :
    a = 30
    b = 0
    results = a / b
    print(results)

except ZeroDivisionError :
    print("Division by zero")






        



