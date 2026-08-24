# String Basics
experiment = "Physics Experiment"
length = len(experiment)
print(f"Length: {length}")
print(f"Experiment. {experiment}")
upper_name = experiment.upper()
print(f"Uppercase: {upper_name}")
lower_name = experiment.lower()
print(f"Lowercase: {lower_name}")
if "Chemistry" in experiment:
    print("This is a physics experiment")
new_name = experiment.replace("Physics", "Chemistry")
print(f"New experiment: {new_name}")

