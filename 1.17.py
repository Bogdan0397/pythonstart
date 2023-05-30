m = float(input("Input water mass: "))
T = float(input("Input necessary temperature in Celsuim degrees: "))

J_TOKWH = 2.77778e-7
C = 4.186

q = m*C*T

print("Necessary energy is: ", q, "Joules")

kwh = q*J_TOKWH
cost = kwh*8.9

print("kw/h needed for heating this water is: ", kwh , "which costs:%.2f" %cost, " cents")