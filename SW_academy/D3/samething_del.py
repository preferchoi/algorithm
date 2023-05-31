for test in range(1, 11):
    N_PAS = input().split(' ')
    N = int(N_PAS[0])
    PAS = list(map(str, N_PAS[1]))
    X = True
    i = 0
    while X:
        if PAS[i] == PAS[i+1]:
            PAS.pop(i)
            PAS.pop(i)
            i = -1
        i += 1
        if len(PAS)-1 == i:
            X = False
    print(f'#{test}', end=" ")

    for i in range(len(PAS)):
        print(PAS[i], end="")
    print()