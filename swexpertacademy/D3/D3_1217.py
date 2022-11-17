def popopo(n, m):
    if m == 1:
        return n
    return n * popopo(n, m-1)
for i in range(10):
    test = input()
    nm = input().split(" ")
    print(f'#{test}', end=" ")
    print(popopo(int(nm[0]), int(nm[1])))