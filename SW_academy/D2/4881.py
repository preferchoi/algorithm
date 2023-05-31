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


def q(lst, cur, deep):
    global minV
    deep += 1
    for num in range(N):
        if not num in lst:
            tmp = cur + N_list[deep][num]
            if tmp < minV:
                q(lst + [num], tmp, deep)
    if deep == N:
        minV = cur
        return


for tc in range(1, 1 + int(input())):
    N = int(input())
    N_list = [list(map(int, input().split())) for _ in range(N)]

    minV = 0
    for i in N_list:
        minV += sum(i)

    q([], 0, -1)

    print(f'#{tc} {minV}')
