for tc in range(1, 1+ int(input())):
    N_list = list(map(int, input().split()))
    # print(N_list)
    N_list.remove(max(N_list))
    N_list.remove(min(N_list))
    # print((N_list))
    print(f'#{tc} {round(sum(N_list)/len(N_list))}')