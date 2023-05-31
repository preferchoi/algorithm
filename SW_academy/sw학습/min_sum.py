'''
3
3
1 2 3
2 3 4
3 4 5
4
2 4 1 3
1 1 7 1
9 1 7 10
5 7 2 4
5
6 7 1 10 2
10 2 7 5 9
9 3 2 9 6
1 6 8 2 9
8 3 8 2 1

'''
'''
1턴 [0,0]
2턴 [1,0] [0,1]
3턴 [2,0] [1,1] [0,2]
4턴 [3,0] [2,1] [1,2] [0,3]
5턴 [3,1] [2,2] [1,3]
6턴 [3,2] [2,3]
7턴 [3,3]
'''


def go(N, x, y, all):
    all += N_list[x][y]
    if x == N-1 and y == N-1:
        set_list.append(all)
        return set_list

    if x == N-1:
        go(N, x, y+1, all)
    elif y == N-1:
        go(N, x+1, y, all)
    else:
        go(N, x+1, y, all)
        go(N, x, y+1, all)


for test in range(int(input())):
    N = int(input())
    N_list = []
    for i in range(N):
        N_list.append(list(map(int, input().split(" "))))
    # print(N_list)

    x = 0
    y = 0
    all = 0
    Min = 999
    set_list = []

    go(N, 0, 0, 0)

    print(f'#{test+1}', min(set_list))