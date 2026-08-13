



def calculate_final_velocity(initial_velocity, acceleration, time):
    V = initial_velocity + (acceleration * time)
    return V

U= float(input("Initial velocity (m/s): "))
A= float(input("Acceleration (m/s^2): "))
T= float(input("Time (s): "))

V = calculate_final_velocity(U, A, T)
print(f"The final velocity is {V} m/s.")

print("PROGRAM FINISHED")