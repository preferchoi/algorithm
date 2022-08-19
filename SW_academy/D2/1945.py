for tc in range(1, 1 + int(input())):
    N = int(input())
    ans_list = [0 for _ in range(5)]
    while N > 1:
        if not N % 2:
            ans_list[0] += 1
            N //= 2
        if not N % 3:
            ans_list[1] += 1
            N //= 3
        if not N % 5:
            ans_list[2] += 1
            N //= 5
        if not N % 7:
            ans_list[3] += 1
            N //= 7
        if not N % 11:
            ans_list[4] += 1
            N //= 11
    print(f'#{tc}', end=' ')
    print(*ans_list)
