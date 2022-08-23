
def cut_list(N_list, N_idx_list):
    if len(N_list) > 1:
        L_list, R_list = [N_list[:(len(N_list) + 1) // 2], N_list[(len(N_list)+1) // 2:]]
        L_idx_list, R_idx_list = [N_idx_list[:(len(N_idx_list)+1) // 2], N_idx_list[(len(N_idx_list)+1) // 2:]]
    if len(L_list) > 1:
        L_list, L_idx_list = cut_list(L_list, L_idx_list)

    if len(R_list) > 1:
        R_list, R_idx_list = cut_list(R_list, R_idx_list)

    return [L_list, R_list], [L_idx_list, R_idx_list]


def winner(N_list, N_idx_list):
    global dep

    L_list, L_idx_list = N_list[0], N_idx_list[0]
    R_list, R_idx_list = N_list[1], N_idx_list[1]

    if len(L_list) >= 2:
        L_list, L_idx_list = winner(L_list, L_idx_list)
    if len(R_list) >= 2:
        R_list, R_idx_list = winner(R_list, R_idx_list)

    dep += 1
    # print(dep, 'N_list', N_list, 'L_list', L_list, 'R_list', R_list)

    if len(L_list) == 1 and len(R_list) == 1:
        if L_list[0] == 1:
            if R_list[0] == 2:
                return R_list, R_idx_list
            else:
                return L_list, L_idx_list
        elif L_list[0] == 2:
            if R_list[0] == 3:
                return R_list, R_idx_list
            else:
                return L_list, L_idx_list
        elif L_list[0] == 3:
            if R_list[0] == 1:
                return R_list, R_idx_list
            else:
                return L_list, L_idx_list

    return L_list, L_idx_list


for tc in range(1, 1 + int(input())):
    N = int(input())
    N_list = list(map(int, input().split()))
    N_idx_list = list(range(1, N + 1))

    dep = 0
    N_list, N_idx_list = cut_list(N_list, N_idx_list)
    ans, ans_idx = winner(N_list, N_idx_list)

    print(f'#{tc} {ans_idx[0]}')