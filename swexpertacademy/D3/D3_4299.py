for test in range(1, int(input())+1):
    DHM = list(map(int, input().split(" ")))
    D, H, M = DHM[0], DHM[1], DHM[2]

    count_D = D - 11
    count_H = H - 11
    count_M = M - 11

    Kicked = count_D*24*60 + count_H*60 + count_M

    if Kicked < 0:
        print(f'#{test}', '-1')
    else:
        print(f'#{test}', Kicked)