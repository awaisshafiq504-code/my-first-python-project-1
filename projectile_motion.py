print()

import math
import numpy as np
vo = float(input(" initial velocity (m/s): "))
angle= float(input(" launch angle (degrees): "))

angle_rad = math.radians(angle)

vx = vo * math.cos(angle_rad)
vy = vo * math.sin(angle_rad)

print("Horizontal  velocity:", vx, "m/s")
print("Vertical  velocity:", vy, "m/s")
g= 9.81

flight_time = (2 * vy) / g
print("Flight time:", flight_time, "s")
max_height = (vy**2) / (2 * g)
range_distance = vx * flight_time
print("Maximum height:", max_height, "m")
print("Range:", range_distance, "m")


time = np.linspace(0, flight_time, num=100)

x = vx * time
y = vy * time - 0.5 * g * time**2
import matplotlib.pyplot as plt
plt.plot(x, y)
max_X = vx * (vy / g)
plt.scatter(max_X, max_height)
plt.text(max_X, max_height, f"Maximum height = {max_height:.2f} m")

plt.scatter(range_distance, 0)
plt.text(range_distance, 0, "Landing point")
plt.text(range_distance, 1, f"Range = {range_distance:.2f} m")

plt.title(f"projectile motion: {vo} m/s at {angle}°")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Height (m)")
plt.grid(True)

plt.savefig("projectile_motion.png", dpi=300)
plt.show()
print("PROGRAM FINISHED")
