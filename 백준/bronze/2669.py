
N_list = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y2 - y1):
        for x in range(x2 - x1):
            N_list[y1 + y][x1 + x] = 1

sumV = 0
for i in N_list:
    sumV += sum(i)
print(sumV)
