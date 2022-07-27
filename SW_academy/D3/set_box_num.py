for test in range(1, int(input())+1):
    NQ = list(map(int, input().split(" ")))
    N, Q = NQ[0], NQ[1]
    array = [0]*N
    for i in range(Q):
        LR = list(map(int, input().split(" ")))
        L, R = LR[0]-1, LR[1]
        for j in range(L, R):
            array[j] = i+1
    print(f'#{test}', end=" ")
    for i in array:
        print(i, end=" ")
    print()