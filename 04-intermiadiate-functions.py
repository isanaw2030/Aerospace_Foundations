# functions calling functions

def add(a, b):
    return(a + b)

def square(x):
    return(x * x)

results = square(add(2, 3))

print(results) # output = (2 + 3) = 5, (5 * 5) = 25

# Default parameters

def greet(name="Engineer"):
    print("Hello", name)

greet() # still works even without passing an argument - very practical in larger systems
greet("Isana")

# Returning Multiple values

def calculatuons(a, b):

    return(a + b, a - b, a * b, a / b)

sum_result, minus_result, multiply_result, division_result = calculatuons(8, 2)

print(f"sum results: {sum_result}")
print(f"Minus results: {minus_result}")
print(f"Multiply results: {multiply_result}")
print(f"Division results: {division_result:.2f}")

# functions inside loop

def square(n):
    return(n ** 2)
for number in range(10):
    results = square(number)
    print(results)




# Build a reusable Physics Tools

def force(mass, accelaration):
    return(mass * accelaration)

f = force(10, 9.8)

print(f"Force = {f:.2f}N")


# function calling function 

def rocket(speed):
    return(speed + 100)

def booster(power):
    return rocket(power) * 2

result = booster(50)

print(result) # Output = (booster power = 50), booster function calls rocket function as power = 50, becomes a parameter inside rocket function, speed is returned as 50 + 100 = 150. get multiplied by 2 in booster function to get 300 which is stored as result!



def add(a, b):
    return(a + b)

def double(x):
    return(x * 2)

output = double(add(4, 6))

print(output)


def rocket(speed):
    return speed + 50

def booster(power):
    return(rocket(power * 2))

check = booster(25)

print(check)


def first(x):
    return(x + 3)

def second(y):
    return(first(y) * 2)

def third(z):
    return(second(z) - 4)

analysis = third(5)

print(analysis)

# variable tracking

def engine(force):
    return(force + 20)

thrust = engine(30)

thrust = thrust * 3

print(thrust)


def alpha(a):
    return(a * 2)

def beta(b):
    return(alpha(b + 3))

def gamma(c):
    return(beta(c) - 5)

display = gamma(7)

print(display)



# scope and Data flows - scope: where a variable is accessible

def rocket():
    fuel = 500
    print(f"Fuel = {fuel}")

rocket() 
#print(fuel) # causes an error- variable fuel is only accessible inside function


# Global variable - created outside function

fuel = 700

def rocket():
    print(f"fuel: {fuel}")

rocket()
print(fuel) # now this works perfectly fine!

# Combining Local vs Global variable

x = 10

def test():
    x = 5
    print(x)

test()

print(x)

# output
# 5
# 10
# Variables can have SAME NAME but exist in DIFFERENT scopes

fuel = 500

#def launch():
  #  fuel = fuel + 100 # this cause an error
 #   print(fuel)

#launch() 

def launch():
    fuel_level = fuel + 100 # this works
    print(fuel_level)

launch()

# Example

gravity = 9.8 # Global variable

def calculate_weight(mass):
    return(mass * gravity)

weight = calculate_weight(50)

print(f"Weight = {weight:.2f}N")


# lambda function - tiny one- line functions

# Example 1

# getting square of a number using lambda function

square = lambda n: n * n

result = square(6)
print(result)

# Example 2 - adding two numbers using lambda functions

sum = lambda a, b: a + b

sum_result = sum(10, 20)

print(sum_result)

