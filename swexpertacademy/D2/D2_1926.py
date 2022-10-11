N = int(input())
for i in range(1, N+1):
    count = 0
    k = i % 100
    if i // 100 == 3 or i // 100 == 6 or i // 100 == 9:
        print('-', end='')
        count += 1
    j = i % 10
    if k // 10 == 3 or k // 10 == 6 or k // 10 == 9:
        print('-', end='')
        count += 1
    if j == 3 or j == 6 or j == 9:
        print('-', end='')
        count += 1
    if count == 0:
        print(i, end="")
    print(end=' ')