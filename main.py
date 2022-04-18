a, b = int(input()), int(input())
num_max = 0
num_sum = 0
for i in range(a, b + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += j
            if count >= num_sum:
                num_sum = count
                num_max = j
print(num_max, num_sum, sep=' ')
