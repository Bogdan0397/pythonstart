def lst_sum(l):
    if len(l)==0:
        return 0
    else:
        return l[0] + lst_sum(l[1:])


print(lst_sum(list(map(int, input().split()))))

print("TEST"*100)
print("HI")
print("1 more test")