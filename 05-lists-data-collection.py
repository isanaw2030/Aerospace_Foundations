# lists - a list store multiple values in one variable

temperatures = [100, 200, 300, 400, 500, 600]

print(temperatures)
print(type(temperatures))

# accessing elements from list - using indexes
# computer loves couting from zero!

element1 = temperatures[0]
element2 = temperatures[1]
element3 = temperatures[2]
element4 = temperatures[3]
element5 = temperatures[4]
element6 = temperatures[5]

print(element1)
print(element2)
print(element3)
print(element4)
print(element5)
print(element6)

# accessing last element: -1

last_element = temperatures[-1]

print(last_element)

# Total number of elements - len()

number_of_items = len(temperatures)
print(number_of_items)

# changing elements in a list - lists are mutable meaning they can be changed and modified

scores = [80, 78, 67, 90, 36, 45]

# changing 36 to 70

new_score = 70

scores[4] = new_score
print(scores)

# adding elements to a list - append()

prices = [1400, 3500, 7800, 10000]
print(len(prices))
# add 5000 to a list

prices.append(5000)
print(prices)

print(len(prices))


# removing elements from a list - remove()

rockets = ["Falcon", "Starship", "Artemis"]
print(len(rockets))
rockets.remove("Artemis")
print(rockets)
print(len(rockets))


# loop + list 

products = ["Laptop", "Tablet", "Phone", "Ipad"]

for item in products:
    print(item)

# better version - getting items with their indexes - enumerate()

for index, items in enumerate(products):
    print(index, items)

# list + function

def square(number):

    return(number ** 2)

numbers = [1, 2, 3, 4, 5, 6]

for n in numbers:
    results = square(n)
    print(results)

double = lambda number: number * 2

values = [1, 3, 5, 7, 9]

for  v in values:
    results = double(v)
    print(results)

# list can contain different data types

data = [122, "python", True]

print(type(data[0]))
print(type(data[1]))
print(type(data[-1]))

# scope + list


fuel_levels = [100, 95, 90, 85, 80]

def modify():
    fuel_levels[-1] = 78

modify()

print(fuel_levels)

# simple program

def greetUser():
    user = input("Enter your name:")
    return user


def validate_user_name():
    user_name = greetUser()

    while user_name == "":
        print("Invalid option.")
        user_name = greetUser()
    
    print("Welcome", user_name)


def input_rocket():
    name = input("Enter name of a rocket: ").strip()
    return name

def is_meaningful_name(name):
    name_lower = name.lower()

    # reject too short name

    if len(name_lower) < 3:
        return False

    # reject pure intergers

    if name_lower.isdigit():
        return False

    # accepts classic structured names (falcon, Artemis)
    # if it contains a hyphen and atleast one letter, its highly likely valid

    if "-" in name_lower and any(char.isalpha() for char in name_lower):
        return True

    # Catch keyboard smashes (like kjhg, sdfr) by checking vowels
    # Real word/names almost always contains atleast one vowel (a, e, i, o, u, y)

    vowels = "aeiouy"
    has_vowel = any(char in vowels for char in name_lower)

    if not has_vowel:
        return False
    return True


def validate_input():
    rocket = input_rocket()

    while rocket == "" or not is_meaningful_name(rocket):
        print("❌ Invalid rocket name! Please use a meaningful name (eg, falcon, mk-17)")
        print("👉 Avoid random keys (jhygl, sdgfrt) or simple numbers/letters (1, 2f, f)")
        print("====================================================================")
        rocket = input_rocket() # ask them again until a valid rocket name is provided

    print(f"\n🚀 SUCCESS: Rocket '{rocket.title()}' has been verified and registered for assembly 🛰️")


print("================== Aerospace Space Validation System ==================")

validate_user_name()
validate_input()