import math

r = float(input("Pls inpunt radius: "))

circule_area = math.pi*pow(r,2)
ball_volume = (4/3)* math.pi*pow(r,3)

print("Area of circule with radius" ,r, " radius is: %.2f"% circule_area)
print("Volume of ball with ", r, " radius is: %.2f"% ball_volume)