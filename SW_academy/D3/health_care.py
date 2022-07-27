T = int(input())

for test in range(1, T+1):
    LUX = input().split(" ")
    L, U, X = int(LUX[0]), int(LUX[1]), int(LUX[2])
    print(f'#{test}', end=" ")
    if L <= X <= U:
        print('0')
    else:
        if L > X:
            print(L-X)
        elif U < X:
            print('-1')