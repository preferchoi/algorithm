from itertools import permutations


def find():
    mv = 100
    for p in permutations(range(N)):
        sv = 0
        for i in range(N):

            sv += lst[i][p[i]]

            sv += aaaaaa[i][p[i]]

        if mv > sv:
            mv = sv
    return mv


for tc in range(1, 1 + int(input())):
    N = int(input())

    lst = [list(map(int, input().split())) for _ in range(N)]
    aaaaaa = [list(map(int, input().split())) for _ in range(N)]

    print('#{} {}'.format(tc, find()))