a = int(input())
count = 0
while a >= 25:
    count += 1
    a -= 25
while a >= 10:
    count += 1
    a -= 10
while a >= 5:
    count += 1
    a -= 5
while a >= 1:
    count += 1
    a -= 1
print(count)
