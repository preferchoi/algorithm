'''
3
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8

'''
from itertools import permutations

for tc in range(1, 1 + int(input())):
    N = int(input())
    N_list = [list(map(int, input().split())) for _ in range(N)]

    minV = 100

    for p in permutations(range(N)):
        sumV = 0
        for i in range(N):
            sumV += N_list[i][p[i]]

        if minV > sumV:
            minV = sumV

    print(f'#{tc} {minV}')
#









