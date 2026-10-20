# Modules & Code Organization
# module - is just another python file with reusable code
# modules makes programs projects clean, easy to debug and easy to expand
# I will create these file - rocket_math.py for calculations, mission_log.py to save reports, mission_safety.py to handle errors and programs safety, mission_control(main.py) to assembles everything

# Welcome to beginner modules and code organization !


# built-in-modules/libraries

import math

def get_sqt(number):
    return (math.sqrt(number))

print(get_sqt(81))
print(get_sqt(54))

import time

print("Mission starting ...")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
print("Launch 🚀")


import numpy as np

matrix_a = np.array([5, 7])
matrix_b = np.array([10, 49])

dot_ab = np.dot(matrix_a, matrix_b)

displacement = np.linalg.norm(dot_ab)
print(f"Displacement : {displacement :.2f} km")

import random
print(random.randint(1, 9)) # result is not fixed, changes per each run!

weather_conditions = ["WINDY", "RAINY", "CLOUDY", "CALM", "STORMY"]

print(random.choice(weather_conditions))

print("\n-------- Let\'s play this a while ---------\n")

def get_ai_turn():
    """"Simulates the AI selecting a weather condition."""
    time.sleep(1.5)
    choice = random.choice(weather_conditions)
    print(f"AI executes : {choice}")
    return choice

def get_human_turn():
    """Simulates the human selecting a weather condition"""
    time.sleep(1.5)
    choice = random.choice(weather_conditions)
    print(f"Human executes : {choice}")
    return choice

print("\n============== WEATHER WARFARE: AI vs HUMAN ==============\n")

turn_count = 0
max_turns = 10  # Maximum turn limit

while True:
    turn_count += 1
    print(f"\n------ ROUND {turn_count} ---------")

    # AI turn
    ai_weather = get_ai_turn()

    if ai_weather == "STORMY":  # check for critical weather condition (STORMY)
        print("\nGAME OVER : The AI generated a STORMY system! Atmospheric collapse. Human wins.")
        break
    
    # Human turn
    human_weather = get_human_turn()

    # check for same critical weather condition (STORMY)
    if human_weather == "STORMY":
        print("\nGAME OVER : You generated a STORMY system! Radar track tracking lost. AI wins!")
        break

    # Match/clash check (sudden death)

    if ai_weather == human_weather:
        print(f"\n SUDDEN DEATH : Both systems generated '{ai_weather}' simultaneously! The game is a tie.")
        break

    # turn limit guard

    if turn_count >= max_turns:
        print("\nGAME OVER : Maximum mission duration reached! It's a draw!")
        break

    print("\n==================== Mission Closed ==================")





