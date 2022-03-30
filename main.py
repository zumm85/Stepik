n = int(input())
fib = 1
fib1 = 0
for i in range(1, n + 1):
    fib2 = fib
    fib = fib2 + fib1
    fib1 = fib2
    print(fib1, end=' ')
