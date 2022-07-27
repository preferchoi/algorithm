for test in range(1, int(input()) + 1):
    MD = list(map(int, input().split(" ")))
    T_m, T_d = MD[0], MD[1]
    S_m, S_d = 1, 1
    M_D_dir = {"1": 31, "2": 29, "3": 31, "4": 30, "5": 31, "6": 30,
               "7": 31, "8": 31, "9": 30, "10": 31, "11": 30, "12": 31}
    sum = T_d - 1

    while T_m != S_m:
        sum += M_D_dir[str(S_m)]
        S_m += 1

    date = sum%7 + 4
    if date >= 7:
        date -= 7
    print(f'#{test}', date)
