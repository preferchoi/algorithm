'''
1
7 3 6 4 2 9 5 8 1
5 8 9 1 6 7 3 2 4
2 1 4 5 8 3 6 9 7
8 4 7 9 3 6 1 5 2
1 5 3 8 4 2 9 7 6
9 6 2 7 5 1 8 4 3
4 2 1 3 9 8 7 6 5
3 9 5 6 7 4 2 1 8
6 7 8 2 1 5 4 3 9

1
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9

1
1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2
3 3 3 3 3 3 3 3 3
4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9

'''

for tc in range(1, 1 + int(input())):
    N_list = [list(map(int, input().split())) for _ in range(9)]

    key = set(range(1, 10))
    ans = 1
    for y in range(9):
        tmp = set()
        tmp2 = set()
        for x in range(9):
            tmp.add(N_list[y][x])
            tmp2.add(N_list[x][y])
        if key != tmp or key != tmp2:
            ans = 0
            break
        if not ans:
            break
    if ans:
        for y in range(0, 9, 3):
            for x in range(0, 9, 3):
                tmp = []
                for i in range(3):
                    tmp += N_list[y + i][x:x + 3]

                if key != set(tmp):
                    ans = 0
                break
            if not ans:
                break
    print(f'#{tc} {ans}')
