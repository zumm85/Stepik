n = int(input())
x3 = 0
countlast = 0
x2 = 0
x5 = 0
x7 = 1
x05 = 0
last = n % 10
while n > 0:
    a = n % 10
    if a == 3:
        x3 += 1
    if a == last:
        countlast += 1
    if a % 2 == 0:
        x2 += 1
    if a >5:
        x5 += a
    if a > 7:
        x7 *= a
    if a == 0 or a == 5:
        x05 += 1
    n //= 10
print(x3, countlast, x2, x5, x7, x05, sep="\n")
