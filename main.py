n = int(input())
counter1 = 0
counter2 = 0
for i in range(1, n + 1):
    n = int(input())
    if n > counter1:
        counter2 = counter1
        counter1 = n
    elif n < counter1 and n > counter2:
        counter2 = n

print(counter1, counter2, sep = '\n')
