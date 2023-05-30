change = int(input("Pls input your exchange in us cents: "))

CENTS_PER_TONIE = 200
CENTS_PER_LONIE = 100
CENTS_PER_QUARTER = 25
CENTS_PER_DIME = 10
CENTS_PER_NICKEL = 5

print("tonnie is: ", change // CENTS_PER_TONIE)

change = change % CENTS_PER_TONIE
print(change)

print("lonnie is: ", change // CENTS_PER_LONIE)

change = change % CENTS_PER_LONIE

print("quarter is: ", change // CENTS_PER_QUARTER)

change = change % CENTS_PER_QUARTER

print("dime is: " , change // CENTS_PER_DIME)

change = change % CENTS_PER_DIME

print("nickel is: ", change // CENTS_PER_NICKEL)

change = change % CENTS_PER_NICKEL

print ("cents ", change)