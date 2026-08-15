# Force to acceleration.py
# This program calculates acceleration given force and mass using Newton's Second Law of Motion.
def calculate_acceleration(force, mass):
    if mass <= 0:
        raise ValueError("Mass must be greater than zero.")
    acceleration = force / mass  # Using the formula a = F / m
    return acceleration
F = float(input("Force (N): "))
m = float(input("Mass (kg): "))
a = calculate_acceleration(F, m)
print(f"The acceleration is {a} m/s^2.")