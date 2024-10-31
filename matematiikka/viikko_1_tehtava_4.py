import numpy as np

# Tehtävä 1
print(f"1.a. vastaus: {np.degrees(2.493)} astetta")
print(f"1.b. vastaus: {np.degrees(0.911)} astetta")

# Tehtävä 2
print(f"2.a. vastaus: {np.radians(137.7)} radiaania")
print(f"2.b. vastaus: {np.radians(62.3)} radiaania")

# Tehtävä 3
A = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])
print("3. vastaus:")
for i in A:
    print(f"{i} astetta on {np.radians(i)} radiaania.")