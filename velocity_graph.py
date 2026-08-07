
import matplotlib.pyplot as plt
u=5
a=2

time=[0,1,2,3,4,5]
velocity=[]
for t in time:
    v= u + a*t
    velocity.append(v)

print(velocity) 
plt.plot(time, velocity, marker="o")
plt.title("velocity vs Time")
plt.xlabel("Time(s)")
plt.ylabel("Velocity (m/s)")
plt.grid(True)

plt.savefig("velocity_graph.png",dpi=300)
plt.show()

