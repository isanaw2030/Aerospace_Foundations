# Dictionaries - A dictionary stores key value pairs

# Example

rocket = {
    "name": "Artemis",
    "fuel": 90,
    "crew": 4
}

# Accessing Dictionary Values

rocket_name = rocket["name"]
rocket_fuel = rocket["fuel"]
rocket_crew = rocket["crew"]
print("=" * 50)

print(f"Rocket name: {rocket_name}")
print(f"Rocket fuel: {rocket_fuel}")
print(f"Rocket crew: {rocket_crew}")

print("=" * 50)
# Example 2

satellite = {
    "temperature": 120,
    "battery": 80,
    "signal": "strong"
}
print("🛰️ ============ Satellite Data Telemetry ==================== 🛰️")
print(f"Satellite Temperature: {satellite["temperature"]}K")
print(f"Satellite Battery: {satellite["battery"]}%")
print(f"Satellite Signal: {satellite["signal"]}")

print("=" * 50)

# Modifying values - Dictionaries are mutable just like list. Can be changed and modified

# changing rocket fuel above from 90 to 100

rocket["fuel"] = 100
 
print(f"New rocket fuel: {rocket["fuel"]}%")

# change satellite signal from strong to weak

satellite["signal"] = "weak"
print(f"New Satellite Signal: {satellite["signal"]}")

# adding new values to dictionary

rocket["status"] = "Ready"

print(rocket)

# looping through dictionaries

for key in rocket:
    print(key)

# Getting values during loop

for key in rocket:
    print(f"{key} = {rocket[key]}")


# dictionary + conditions

if rocket["fuel"] < 80:
    print("Low fuel warning")


# List of dictionary - Dictionary + lists

rockets = [
    {"name": "Falcon", "fuel": 80},
    {"name": "Artemis", "fuel": 100},
    {"name": "Starship", "fuel": 95}
]

# Loops thrugh them

for rocket in rockets:
    print(rocket["name"])


# list of dictionary + condition

for rock in rockets:
    if rock["fuel"] > 50:
        print(f"{rock["name"]}: Fuel Enough")

    
# checking keys

if "fuel" in rock:
    print("Fuel data exists")


# nested dictionaries - dictionary inside dictionry

flight_mission = {
    "rocket": {
        "name": "Falcon Heavy",
        "fuel": 100
    },
    "crew": {
        "commander": "Brin",
        "engineer": "Damis"
    }
}

# accessing nested data

rocket_name = flight_mission["rocket"]["name"]
rocket_fuel = flight_mission["rocket"]["fuel"]

crew_commander = flight_mission["crew"]["commander"]
crew_engineer = flight_mission["crew"]["engineer"]

print("============= Mission Data Analysis =======================")

print(f"Rocket name: {rocket_name}")
print(f"{rocket_name} Fuel: {rocket_fuel}%")
print(f"Crew Commander: {crew_commander}")
print(f"Crew Engineer: {crew_engineer}")

print("=" * 50)


# statistics from list of dictionaries


missions = [
    {"name": "Falcon", "fuel": 80},
    {"name": "Artemis", "fuel": 55},
    {"name": "Starship", "fuel": 45}
]


total_fuel = 0

for  mission in missions:
    total_fuel += mission["fuel"]

print(f"Total fuel: {total_fuel} pounds")



# mission classification

for mission in missions:

    if mission["fuel"] >= 80:
        print(f"{mission["name"]}: FULLY READY")

    elif mission["fuel"] >= 50:
        print(f"{mission["name"]}: MODERATE")

    else:
        print(f"{mission["name"]}: CRITICAL")

print("=" * 50)


# Functions + Dictionaries

def check_fuel(mission):
    if mission["fuel"] < 50:
        print(f"{mission["name"]}: LOW FUEL ALERT")
    else:
        print(f"{mission["name"]}: FUEL OKAY")

check_fuel({"name": "Artemis", "fuel": 50})
check_fuel({"name": "Falcon", "fuel": 45})
