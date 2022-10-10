for tc in range(1, 1 + int(input())):
    N = int(input())
    N_list = list(map(int, input().split()))
    ans = 0
    # print(N , N_list)
    while N_list:
        cut = N_list.index(max(N_list))
        ans += max(N_list)*len(N_list[:cut])-sum(N_list[:cut])
        del N_list[:cut+1]
        # print(N_list)
    print(f'#{tc} {ans}')