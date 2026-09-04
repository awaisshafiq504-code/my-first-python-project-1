import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

time = np.linspace(0, 30, 3000)

brightness = 1.0 + np.random.normal(0, 0.002, len(time))

for center in [5, 15, 25]:
    transit = np.abs(time - center) < 0.15
    brightness[transit] -= 0.02

normal_brightness = np.mean(brightness)
print(f"Normal brightness: {normal_brightness:.4f}")

dim = brightness < normal_brightness - 0.01
print(f"Number of dim points: {np.sum(dim)}")

dim_indices = np.where(dim)[0]
print("First dim measurement:", time[dim_indices[0]])
print("Last dim measurement:", time[dim_indices[-1]])

gaps = np.diff(dim_indices)

breaks = np.where(gaps > 1)[0]

start_indices = np.insert(breaks + 1, 0, 0)
end_indices = np.append(breaks, len(dim_indices) - 1)

for start, end in zip(start_indices, end_indices):
    center = np.mean(time[dim_indices[start:end + 1]])
    print(f"Transit detected near day {center:.2f}")

transit_times = []

for start, end in zip(start_indices, end_indices):
    center = np.mean(time[dim_indices[start:end + 1]])
    transit_times.append(center)

periods = np.diff(transit_times)
orbital_period = np.mean(periods)

print(f"Estimated orbital period: {orbital_period:.2f} days")

plt.plot(time, brightness)

for transit_time in transit_times:
    plt.axvline(
        transit_time,
        linestyle="--",
        label=f"Transit: {transit_time:.1f} days"
    )

plt.xlabel("Time (days)")
plt.ylabel("Relative brightness")
plt.title("Simulated Exoplanet Transit")
plt.legend()
plt.savefig("expoplanet_transit_analysis.png", dpi=300, bbox_inches="tight")
plt.show()
print("\n--- Scientific Conclusion ---")
print(
    f"Three transit events were detected at approximately "
    f"{transit_times[0]:.2f}, {transit_times[1]:.2f}, and "
    f"{transit_times[2]:.2f} days."
)
print(f"Estimated orbital period: {orbital_period:.2f} days.")
print(
    "The repeated brightness dips are consistent with a "
    "planet passing in front of its host star."
)