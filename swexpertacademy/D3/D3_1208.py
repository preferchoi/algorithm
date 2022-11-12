def solt_2(def_list):
    for _ in range(100):
        for j in range(1, 100):
            if def_list[j] < def_list[j - 1]:
                def_list[j], def_list[j - 1] = def_list[j - 1], def_list[j]
    return def_list


for tc in range(1, 11):
    N = int(input())
    N_list = list(map(int, input().split()))
    N_list = solt_2(N_list)
    # N_max, N_min = 0, 9999

    for i in range(N):
        N_list[0] += 1
        N_list[-1] -= 1
        N_list = solt_2(N_list)

    print(f'#{tc} {N_list[-1] - N_list[0]}')