# Measurements
measurements = {12.5, 18.2, 25.7, 15.5, 20.1}
count = len(measurements)
total = sum(measurements)

average = total / count if count > 0 else 0
highest = max(measurements) if count > 0 else None
lowest = min(measurements) if count > 0 else None
data_range = highest - lowest if count > 0 else None



print(f"The total of measurements is: {total}")
print(f"The average of measurements is: {average}")
print(f"The count of measurements is: {count}")
print(f"The highest measurement is: {highest}")
print(f"The lowest measurement is: {lowest}")
print(f"The range of measurements is: {data_range}")