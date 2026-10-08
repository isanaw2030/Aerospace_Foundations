# loops

import time

# while loop - keeps running a specific code WHILE the condition remains TRUE

# counter

count = 1

while count <= 5:
    print(count)
    time.sleep(1)
    count += 1

# user - controlled loop

password = ""
while password != "rocket":
    password = input("Enter password: ").lower()
    
print("Login successfully ✅")

print("-" * 50)

# for loop - controlled repetition

for  number in range(5):
    print(number)
    time.sleep(1)
print("-" * 50)    

for i in range(1, 5):
    print(i)
    time.sleep(1)

print("-" * 50)

# Nested loops - for multplication table

number = int(input("Enter number: "))

for i in range(10,0,-1):

    print(f"{i} X {number} = {i * number}")


print("-" * 50)
   
# Example 2

for j in range(1, 11):
    print(f"{j} X {number} = {j * number}")

print("-" * 50)

# rocket launch countdown

for countdown in range(10, 0, -1):
    print(countdown)
    time.sleep(1)

print("Lift off 🚀")

print("-" * 100)
# Breaking loops

while True:
    command = input("Type exit to stop: ").lower()

    if command == "exit":
        break

