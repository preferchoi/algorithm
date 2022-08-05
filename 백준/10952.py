'''
1 1
2 3
3 4
9 8
5 2
0 0

'''
while True:
    N, M = map(int, input().split())
    if not N and not M:
        break
    print(N + M)
