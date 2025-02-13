n, m = map(int, input().split())

i = 1
while (n * i) % 10 != m and (n * i) % 10 != 0:
    i += 1

print(i)