N = int(input())

# здесь задается функция fib_rec (переменную N не менять!)
def fib_rec(N,f=[1,1]):
    if len(f)<N:
        f.append(f[-1]+f[-2])
        print(f)
        fib_rec(N,f)

    print(f)


print(fib_rec(6))