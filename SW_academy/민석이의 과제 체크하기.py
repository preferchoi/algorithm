for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    M_list = list(map(int, input().split()))
    # print(N, M, M_list, ans_list)
    # 5 3 [2, 5, 3] [0, 1, 2, 3, 4]
    print(f'#{tc}', end=" ")
    for i in range(1, 1 + N):
        if i not in M_list:
            print(i, end=" ")
    print()
