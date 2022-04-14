a = int(input())
b = 0
c = 0
flag = True
while a != 0:
    b = a % 10
    a = a // 10
    c = a % 10
    if c <= 0:
        c = b
#    print(b)
#    print(c)
    if b > c:
        flag == False
        print('NO')
        break
else:
    print('YES')
