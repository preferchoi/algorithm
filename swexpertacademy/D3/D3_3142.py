for test in range(1, int(input())+1):
    NM = list(map(int, input().split(" ")))
    N, M = NM[0], NM[1]

    for i in range(0, M+1):
        if (M-i) + (2*i) == N:
            print(f'#{test}', M-i, i)