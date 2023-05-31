"""
1
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3

"""

T = int(input())

for test_case in range(1, T+1):
    q = input().split(" ")
    N, M = int(q[0]), int(q[1])

    list = []
    for i in range(N):
        list.append(input().split(" "))
    # print(list)

    for i in range(N):
        for j in range(N):
            list[i][j] = int(list[i][j])
    # print(list)

    max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            num = 0
            # print()
            for a in range(M):
                for b in range(M):
                    num += list[i+a][j+b]
                    # print(i+a, j+b, end=" ")
            if max < num:
                max = num

    print(f'#{test_case}', max)
