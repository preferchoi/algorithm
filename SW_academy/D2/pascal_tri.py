T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    list = [[1]]

    for i in range(2, N+1):
        list.append([0]*i)
    # print(list)

    for i in range(1, N):
        for j in range(len(list[i-1])):
            list[i][j] += list[i-1][j]
            list[i][j+1] += list[i-1][j]
    # print(list)

    print(f'#{test_case}')
    for i in range(N):
        for j in range(len(list[i])):
            print(list[i][j], end=" ")
        print()