from rocket_math import calculate_momentum, orbital_velocity
from mission_log import write_report, read_report

momentum = calculate_momentum()

altitude = float(input("Enter height above Earth surface(km) : "))

orbital_velocity_calculator = orbital_velocity(altitude)

print("\n--------- Momentum Calculator ----------")
print(f"Momentum : {momentum} kg.m/s")
print("----------------------------")
if momentum > 5000:
    print("HIGH MOMENTUM VEHICLE")
else:
    print("NORMAL MOMENTUM VEHICLE")

print("\n============ Orbital Velocity Estimator ===============")

print(f"Altitude : {altitude} km")
print(f"Orbital Velocity : {orbital_velocity_calculator / 1000 :.2f} km/s")

print("\n----------- Report Generator ---------------")


report = write_report()
generate = read_report()
print(generate)


