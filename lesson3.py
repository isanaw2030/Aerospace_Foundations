# Functions - reusable block of code

# defining a function - def()

def greet():
    print("Hello Engineer 🚀")

# calling a function to run it! - greet()

greet()
# You can pass parameters inside function - makes function powerful

# greet Isana

def sayHi(name):  # name is a parameter
    print("Hi",name)

sayHi("Isana")

print("-" * 50)

# - Example 2 - square of a number

def square(number):
    print(number * number)

square(4)

# Returning values - Function can send results back - return()

# Example 1

def add(a, b):
    return(a + b)

# using it

result = add(3, 5)

print(result)

print("-" * 50)

# Example 2 - momentum calculator

def momentum(mass, velocity):
    return(mass * velocity)

p = momentum(40, 50)

print(f"Momentum = {p}kg.m/s")

# you can calculate momentum as many as you want without rewritting formula repeatedly!
print(momentum(120, 100))
print(momentum(200,240))

print("-" * 50)

# you can pass the returned value somewhere else - powerful

def add_numbers(x, y):
    return(x + y)

result = add_numbers(3, 2)

print(result * 2) # Output = (3 + 2) = 5, (5 * 2) = 10

# local variable - variable inside functions

def test():
    x = 3
    print(x)
test() # This works
#print(x) # this causes an error! - as x exists inside function - scope

print("-" * 50)
# multiple functions

def greet_user(user):
    print("welcome", user)

def launch(rocket):
    print(rocket,"is launching!")

greet_user("Zolet")
launch("Falcon")

