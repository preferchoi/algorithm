'''
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4
'''
N, M = map(int, input().split())

mapp = []
for _ in range(N):
    mapp.append(list(map(int, input().split())))

for _ in range(M):

    x1, y1, x2, y2 = map(int, input().split())
    sumV = 0

    for i in range(x1 - 1, x2):
        sumV += sum(mapp[i][y1 - 1:y2])

    print(sumV)