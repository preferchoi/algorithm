'''
1
5
14054
44250
02032
51204
52212

5*5

0,0 0,1 0,2 0,3 0,4
1,0 1,1 1,2 1,3 1,4
2,0 2,1 2,2 2,3 2,4
3,0 3,1 3,2 3,3 3,4
4,0 4,1 4,2 4,3 4,4

        0,2
    1,1 1,2 1,3
2,0 2,1 2,2 2,3 2,4
    3,1 3,2 3,3
        4,2
'''
for tc in range(1, 1 + int(input())):
    N = int(input())
    N_list = [list(map(int, input())) for _ in range(N)]
    div = N // 2
    sumV = 0
    for i in range(div + 1):
        sumV += N_list[i][div]
        for j in range(1, 1 + i):
            sumV += N_list[i][div + j]
            sumV += N_list[i][div - j]

    for i in range(N - 1, div, -1):
        sumV += N_list[i][div]
        for j in range(1, N - i):
            sumV += N_list[i][div + j]
            sumV += N_list[i][div - j]

    print(f'#{tc} {sumV}')
