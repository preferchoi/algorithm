for tc in range(1, 11):
    N = int(input())
    N_list = list(map(int, input().split()))
    M = int(input())
    M_list = list(input().split())
    # print(N, M, len(N_list), len(M_list))

    for i in range(len(M_list)):
        if M_list[i] == 'I':
            for j in range(int(M_list[i+2])):
                N_list.insert(int(M_list[i+1])+j, int(M_list[i+j+3]))
        elif M_list[i] == 'D':
            for j in range(int(M_list[i+2])):
                del N_list[int(M_list[i+1])]
        elif M_list[i] == 'A':
            for j in range(int(M_list[i+1])):
                N_list.append(M_list[i+j+2])
        else:
            pass

    print(f'#{tc}',end=' ')
    for i in N_list[:10]:
        print(i, end=' ')
    print()
