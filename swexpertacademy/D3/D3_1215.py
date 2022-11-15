for test in range(10):
    N = int(input())

    list = []

    for i in range(8):
        list_inner = []
        abc = input()
        for j in range(8):
            list_inner.append(abc[j])
        list.append(list_inner)
    count = 0
    for i in range(8):
        for j in range(8-N+1):
            r_list = list[i][j:j+N]
            r_list.reverse()
            if list[i][j:j+N] == r_list:
                count += 1

            r_list = []
            for k in range(N):
                r_list.append(list[j+k][i])
            s_list = r_list.copy()
            s_list.reverse()
            if r_list == s_list:
                count += 1
    print(f'#{test+1}', count)