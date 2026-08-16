# Distance with Acceleration Calculator
# This program calculates the distance traveled given initial velocity, time, and acceleration
def calculate_distance_with_acceleration(initial_velocity, time, acceleration):
    distance = (initial_velocity * time) + (0.5 * acceleration * time ** 2)
    return distance
V = float(input("Initial Velocity (m/s): "))
T = float(input("Time (s): "))
A = float(input("Acceleration (m/s^2): "))
D = calculate_distance_with_acceleration(V, T, A)
print(f"The distance traveled is {D} meters.")