# числа Фибоначи
# рекурсивный алгоритм
def fib_r (n):
    if n<=1:
        return n
    return (fib_r(n-1)+fib_r(n-2))

print (fib_r(4))

# алгоритм не использующий рекурсию
def fib (n):
    fib = [0, 1] + [0]*(n-1)
    for i in range (2, n+1):
        fib[i]=fib[i-1]+fib[i-2]

    print (fib)
    
    return fib[n]

print (fib(4))