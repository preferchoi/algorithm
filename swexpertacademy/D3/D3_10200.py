T = int(input())
for test in range(1, T+1):

    # if X[len(X) - 1] == '':
    #     X.pop(len(X) - 1)
    array = list(map(int, input().split(" ")))
    N, A, B = array[0], array[1], array[2]

    Min = A + B - N
    if Min < 0:
        Min = 0
    Max = A
    if A > B:
        Max = B

    print(f'#{test}', Max, Min)

    