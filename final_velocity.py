



def calculate_final_velocity(initial_velocity, acceleration, time):
    V = initial_velocity + (acceleration * time)
    return V

U= float(input("Initial velocity (m/s): "))
A= float(input("Acceleration (m/s^2): "))
T= float(input("Time (s): "))

V = calculate_final_velocity(U, A, T)
print(f"The final velocity is {V} m/s.")
if abs(V) > abs(U):
         print("Speeding up")
elif abs(V) < abs(U):
        print("Slowing down")
else:
            print("constant speed")

print("PROGRAM FINISHED")