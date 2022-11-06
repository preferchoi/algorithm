for test in range(1, int(input())+1):
    DLN = list(map(int, input().split(" ")))
    D, L, N = DLN[0], DLN[1], DLN[2]
    sum = 0
    for i in range(0, N):
        sum += D * (1 + i * L / 100)
    print(f'#{test}', int(sum))
