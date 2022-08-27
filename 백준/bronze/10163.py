
N_list = [[0 for _ in range(1001)] for _ in range(1001)]
N = int(input())
for i in range(1, 1 + N):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2 + y1):
        for x in range(x1, x2 + x1):
            N_list[y][x] = f'{i}'

for i in range(1, 1 + N):
    cnt = 0
    for y in N_list:
        cnt += str(y).count(str(i))
    print(cnt)
