# checking items in a list - "in", "NOT in"

rockets = ["Artemis", "Falcon", "Saturn-V"]
# in
if "Artemis" in rockets:
    print("Rocket exist")

# Not in

if "Starship" not in rockets:
    print("Rocket missing")


# performing math list operations
# summing list values

numbers = [12, 20, 50,60]
total = sum(numbers)

print(f"Total:{total}")

fuel_leves = [100, 95, 90, 85]

print(sum(fuel_leves))

# larget and smallest values

temperatures = [100, 120, 80, 140]

maximum_temperature = max(temperatures)
minimum_temperature = min(temperatures)

print(f"Minimum temperature: {minimum_temperature}")
print(f"Maximum temperature: {maximum_temperature}")

# sorting lists

altitudes = [100, 450, 50, 900, 750, 350, 300, 150, 1000]

# in ascending order

altitudes.sort()

print(f"Sorted altitudes: {altitudes}")

# same you can use sorted()
sorted_altitudes = sorted(altitudes)
print(f"Altitudes: {sorted_altitudes}")

# in descending order - (reverseg=True)

altitudes.sort(reverse=True)

print(f"Reversed altitudes: {altitudes}")

# empty list

products = []

products.append("Laptop")
products.append("Tablet")
products.append("Mobile Phone")
products.append("Ipad")
products.append("Monitor")
print(products)

programming_languages = []
programming_languages.append("Python")
programming_languages.append("Javascript")
programming_languages.append("HTML")
programming_languages.append("CSS")
programming_languages.append("Go")
programming_languages.append("Rust")

print(f"Some of programming languages you can learn: {programming_languages}")

# changing rust to java - list mutability

programming_languages[-1] = "Java"

print(programming_languages)


# building list with user input

cities = []

name = input("Enter two capital cities: ")

cities.append(name)

print(cities)

# loop + condition + list

temperatures = [100, 200, 80, 150]
for temp in temperatures:
    if temp > 100:
        print("Warning", temp)

# list inex tracking - enumerate()

rockets = ["Falcon", "Starship", "Artemis"]

for index, rocket in enumerate(rockets):
    print(index, rocket)

