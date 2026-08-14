# Newton's Second Law of Calculator
def newton_force(mass, acceleration):
    m = float(input("Mass (kg): "))
    a = float(input("Acceleration (m/s^2): "))
    force = m * a  # Using the formula F = m * a
    return force
F = newton_force(0, 0)
print(f"The force is {F} N.")