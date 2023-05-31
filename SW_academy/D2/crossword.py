'''
5<=N<=15
2<=K<=N

1
5 3
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1

1
8 3
1 1 0 1 0 1 1 1
0 1 0 1 0 0 0 1
1 1 1 0 0 1 0 1
0 1 0 1 0 1 1 1
0 0 0 1 0 1 0 1
1 1 1 1 1 1 0 0
0 1 0 0 0 1 0 1
1 1 1 0 1 1 1 1

'''

T = int(input())

for test_case in range(1, T+1):
    n = input().split(" ")
    N = int(n[0])
    K = int(n[1])
    # print('N:', N, 'K:', K)

    # 제약조건
    if not 5 <= N <= 15 or not 2 <= K <= N:
        print('error')
        break

    list = []

    for i in range(N):
        list.append(input().split())
    # print(list)

    '''
    굳이 숫자로 바꿔줘야하나?
    for i in range(N):
        for j in range(N):
            list[i][j] = int(list[i][j])
    print(list)
    '''
    count = 0
    # 가로방향 판독
    for i in range(N):
        for j in range(N-K+1):
            sum = 0
            if j == 0:
                if list[i][j+K] == '0':
                    for c in range(K):
                        sum += int(list[i][j+c])
            elif j+K == N:
                if list[i][j-1] == '0':
                    for c in range(K):
                        sum += int(list[i][j + c])
            else:
                if list[i][j-1] == '0' and list[i][j+K]== '0':
                    for c in range(K):
                        sum += int(list[i][j+c])

            if sum == K:
                count += 1
    # 세로방향 판독
    for i in range(N):
        for j in range(N-K+1):
            sum = 0
            if j == 0:
                if list[j+K][i] == '0':
                    for c in range(K):
                        sum += int(list[j+c][i])
            elif j+K == N:
                if list[j-1][i] == '0':
                    for c in range(K):
                        sum += int(list[j + c][i])
            else:
                if list[j-1][i] == '0' and list[j+K][i]== '0':
                    for c in range(K):
                        sum += int(list[j+c][i])
            if sum == K:
                count += 1
    print(f'#{test_case}', count)


