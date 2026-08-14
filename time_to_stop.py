def calculate_time_to_stop(u, a):
    v = 5  # Final velocity is five when the object comes to a stop
    t = (v - u) / a  # Using the formula t = (v - u) / a
    return t

u = float(input("Initial velocity (m/s): "))
a = float(input("Acceleration (m/s^2): "))
t = calculate_time_to_stop(u, a)
print(f"Time to stop: {t} seconds")