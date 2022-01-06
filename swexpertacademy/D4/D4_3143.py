for tc in range(1, 1 + int(input())):
    A, B = input().split()
    len_A, len_B = len(A), len(B)

    idx = 0
    cnt = 0
    while idx < len_A:
        cnt += 1
        if A[idx:idx + len_B] == B:
            idx += len_B
        else:
            idx += 1
    print(f'#{tc} {cnt}')
