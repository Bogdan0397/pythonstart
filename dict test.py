def give_change(amount):
    a = [0, 0, 0, 0, 0, 0]
    while amount >= 100:
        a[5]+=1
        amount -= 100
    while amount >= 50:
        a[4]+=1
        amount -= 50
    while amount>= 20:
        a[3]+=1
        amount-= 20
    while amount >= 10:
        a[2]+=1
        amount -= 10
    while amount >= 5:
        a[1]+=1
        amount-= 5
    while amount >= 1:
        a[0]+=1
        amount-= 1
    return a
    pass

print(give_change(365))
print(give_change(365))
