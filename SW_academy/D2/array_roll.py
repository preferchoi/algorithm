'''
1
3
1 2 3
4 5 6
7 8 9
'''

T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    list = []

    for i in range(N):
        list.append(input().split())
    # print(list)

    list2 = []
    list3 = []
    list4 = []

    for i in range(N):
        for j in range(N):
            list2.append(list[N-j-1][i])
            list3.append(list[N-i-1][N-j-1])
            list4.append(list[j][N-i-1])
    # print(list2)
    # print(list3)
    # print(list4)
    print(f'#{test_case}')
    for i in range(0, N*N, N):
        for j in range(N):
            print(list2[j+i], end='')
        print(end=" ")
        for j in range(N):
            print(list3[j+i], end='')
        print(end=" ")
        for j in range(N):
            print(list4[j+i], end='')
        print()

