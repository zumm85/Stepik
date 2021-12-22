counter = 0
counter1 = 0
for i in range(1, 11):
    n = int(input())
    if n % 2 == 0:
        counter = n
    else:
        counter1 = n
if counter1 == 0:
    print('YES')
else:
    print('NO')