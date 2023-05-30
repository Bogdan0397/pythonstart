#https://www.youtube.com/watch?v=eI1ZuXVOmng&t=6s&ab_channel=selfedu
a = [-3,1,5,-2,10,-20]

N = len(a)

for i in range(N-1):
    m = a[i]
    p = i
    print(m)
    for j in range(i+1,N):
        if m>a[j]:
            m = a[j]
            p = j
    if i!=p:
        t = a[i]
        a[i] = a[p]
        a[p] = t


print(*a)


