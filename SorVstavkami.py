#https://www.youtube.com/watch?v=jMWvNTp_wFA&ab_channel=selfedu

a = [-3,1,5,-2,10,-20]

N = len(a)

for i in range(1,N):
    for j in range(i,0,-1):
        if a[j]<a[j-1]:
            a[j],a[j-1]=a[j-1],a[j]
        else:
            break

print(*a)