from math import radians
import math

t1 = math.radians(float(input("Pls input latitude of 1 point in degrees: ")))
g1 = math.radians (float(input("Pls input longitude of 1 point in degrees: ")))

t2 = math.radians(float(input("Pls input latitude of 2 point in degrees: ")))
g2 = math.radians (float(input("Pls input longitude of 2 point in degrees: ")))


distance = 6371.01*(math.acos(math.sin(t1)*math.sin(t2) + math.cos(t1)*math.cos(t2)*math.cos(g1 - g2)))

print("Your distance is: ", distance, "km")
