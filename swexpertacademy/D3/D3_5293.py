for t in range(int(input())):

    FF, FT, TF, TT = map(int, input().split(" "))
    # print(FF, FT, TF, TT)
    ans = 0

    if FT == TF == 0 != (TT and FF):
        # N 0 0 N, 1 0 0 1
        print(f'#{t + 1} impossible')  # imp
    elif FT not in [TF - 1, TF, TF + 1]:
        print(f'#{t + 1} impossible')
    else:
        if FT == TF == TT == 0:
            ans = '0' + '0' * FF
            # 3 0 0 0
            # 00 00 00
            # 0000
        elif FT == TF == FF == 0:
            ans = '1' + '1' * TT
            # 0 0 0 3
            # 11 11 11
            # 1111

        elif TF == 0:
            ans = '0' + '0' * FF + '1' * TT + '1'
            # 2 1 0 2
            # 00 00 01 11 11
            # 000111
        elif FT == 0:
            ans = '1' + '1' * TT + '0' + '0' * FF
            # 2 0 1 2
            # 11 11 10 00 00
            # 111000

        elif FT == TF + 1:
            ans = '0' + '0' * FF + '1' * TT + '10' * TF + '1'
            # 4 3 2 1
            # 00 00 00 00 01 11 10 01 10 01
            # 00000110101
        elif FT == TF - 1:
            ans = '1' + '1' * TT + '0' * FF + '01' * FT + '0'
            # 1 2 3 4
            # 11 11 11 10 00 01 10 01 10
            # 11111001010
        elif FT == TF:
            ans = '0' + '0' * FF + '1' * TT + '10' * TF
            # 2 2 2 2
            # 00 00 01 11 11 10 01 10
            # 000111010

        print(f'#{t + 1} {ans}')