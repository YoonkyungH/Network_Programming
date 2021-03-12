sum = 0

for i in range(1, 1001):
    num = i
    for s in str(num):
        sum += int(s)

print(str(sum))