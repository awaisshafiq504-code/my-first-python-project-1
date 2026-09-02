import numpy as np
import matplotlib.pyplot as plt
temperatures = np.array([21, 22, 23, 21, 24, 22, 23, 35, 21, 22], dtype=float)
average = np.mean(temperatures)
print(temperatures)
above_average = temperatures > average
print(temperatures[above_average])
unusual = temperatures > 30
print(temperatures[unusual])
print(f"Average temperatures: {average}")
warmer = temperatures + 5
print(warmer)
difference = temperatures - average 
print(difference)
cleaned = temperatures.copy()
cleaned[cleaned > 30] = np.nan
print(cleaned)
np.mean(cleaned)
average_clean = np.nanmean(cleaned)
print(f"Clean average: {average_clean}")
original_average = np.mean(temperatures)
clean_average = np.nanmean(cleaned)

print("Original average:", original_average)
print("Clean average:", clean_average)
print("Difference:", original_average-clean_average)
change = original_average - clean_average
print(f"Original average: {original_average:.2f} °C")
print(f"Clean average: {clean_average:.2f} °C")
print(f"Change in average: {change:.2f} °C")
standard_deviation = np.nanstd(cleaned)
print(f"Standard deviation: {standard_deviation:.2f} °C")
z_scores = (cleaned - clean_average) / standard_deviation
print("Z_scores:")
print(z_scores)
unusual_z_scores = np.abs(z_scores) > 2
print("Potentially unusual:")
print(temperatures[unusual])



plt.plot(temperatures, label="Original")
plt.plot(cleaned, label="Cleaned")

plt.axhline(
    clean_average,
    linestyle="--",
    label="Clean average"
)

plt.fill_between(
    range(len(cleaned)),
    clean_average - standard_deviation,
    clean_average + standard_deviation,
    alpha=0.2,
    label="±1 standard deviation"
)
for i in np.where(unusual)[0]:
    plt.annotate(
        f"Flagged: {temperatures[i]:.0f} °C",
        (i, temperatures[i]),
        xytext=(i -0.2, temperatures[i] - 1)
    )

z_scores_original = (temperatures - clean_average) / standard_deviation
unusual = np.abs(z_scores_original) > 2

for i in np.where(unusual)[0]:
    print(
        f"Measurement {i + 1}: "
        f"{temperatures[i]:.1f} °C "
        f"→ z-score = {z_scores_original[i]:.2f} "
        f"→ potentially unusual"
    )

plt.xlabel("Measurement")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Data: Before and After Cleaning")
plt.legend()
plt.savefig("temperature_analysis.png", dpi=300, bbox_inches="tight")

plt.show()


plt.plot(temperatures)
plt.axhline(np.nanmean(cleaned), linestyle="--")
bad = temperatures > 30
plt.scatter(np.where(bad)[0], temperatures[bad])
plt.annotate("Possible faulty measurement" , (7, 35), xytext=(5, 32))
plt.plot(temperatures, marker="o")
plt.xlabel("Measurement")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Measurements")
plt.show()   