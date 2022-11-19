T = int(input())
for test in range(1,T+1):
    NM = list(map(int, input().split(" ")))
    N = NM[0]
    M = NM[1]
    if N > 9 or M > 9:
        print(f'#{test} -1')
    else:
        print(f'#{test}', N*M)
