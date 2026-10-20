# We will create two functions - momentum_calculator and orbital_velocity estimator(we enter certain altitude and program roughly computes orbital velocity)

# momentum calculator

def calculate_momentum():
    mass = float(input("Enter mass(kg) : "))
    velocity = float(input("Enter velocity(m\s) : "))
    return (mass * velocity)



# orbital velocity estimator

import math

# constants

G = 6.674e-11           # Gravitational constant
M = 5.972e24            # Mass of Earth (kg)
R = 6.371e6             # Earth Radius (m)


def orbital_velocity(altitude_km):
    r = R + (altitude_km * 1000)  # converting km into meters
    v = math.sqrt(G * M / r)
    return v


