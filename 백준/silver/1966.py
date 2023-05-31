for tc in range(int(input())):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    N_idx_list = list(range(N))
    printing = 0

    cnt = 0
    while True:
        if max(N_list) == N_list[printing]:
            cnt += 1
            N_list.pop(0)
            idx = N_idx_list.pop(0)
            if idx == M:
                break
        else:
            N_list.append(N_list.pop(0))
            N_idx_list.append(N_idx_list.pop(0))
    print(cnt)