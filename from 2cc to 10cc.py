num = input("Input digit: ")

n = len(num)
res = 0

for i in range (n):
    res = res + (int(num[i])*(2**(n-i-1)))
    print (res)

print(res)