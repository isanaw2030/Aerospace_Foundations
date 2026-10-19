# file handling - teaching Programs remember informations
# file =  stored information on the computer eg: .txt, .pdf, .py, .docx

# Opening new file - basic syntax

file = open("telemetry_report.txt", "w") # open a file called telemetry_report.txt in write mode

# Writing inside file

file.write("Falcon mission completed")
file.close() 

# Reading a file

file = open("telemetry_report.txt", "r") # open our file - telemetry_report.txt in read mode

contents = file.read()
print(contents)

# Writing multiple lines to file
# opening same file in write mode - this will erase the old contents

file = open("telemetry_report.txt", "w")
file.write("Rocket Name : Falcon\n")  # \n - adds new line for next sentence
file.write("Fuel : 98%\n")
file.write("Crew : 4\n")

file.close()

file = open("telemetry_report.txt", "r")
contents = file.read()
print(contents)


# append mode -"a"
# Instead of erasing old contents when opening existing files, just append and keep old contents intact!

file = open("telemetry_report.txt", "a")
file.write("-------------------\n")
file.write("Mission Status : Successful\n")
file.write("Warning Counts : 2\n")

file.close()

file.close()

file = open("telemetry_report.txt", "r")
contents = file.read()
print(contents)

# instead of closing file manually, python can handle that using - with open(filename) as file:


with open("mission_report.txt", "w") as file:
    file.write("Average fuel : 97.0 %\n")
    file.write("Maximum altitude : 5500 km\n")
    file.write("Battery charge : 78 %\n")

with open("mission_report.txt", "r") as file:
    contents = file.read()
    print(contents)


def write_report():
    name = input("Enter rocket : ")
    warning_count = int(input("Enter number of warning counts : "))
    fuel = int(input("Enter Fuel amount(%) : "))

    with open("report.txt", "w") as file:
        file.write(f"Rocket Name : {name}\n")
        file.write(f"Warning Counts : {warning_count}\n")
        file.write(f"Fuel Amount : {fuel}%\n")

write_report()

def read_report():
    print("\n ------- Generating Report -----------------")

    with open("report.txt", "r") as file:
        contents = file.read()
        print(contents)

read_report()

