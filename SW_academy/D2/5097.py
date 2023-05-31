'''
3
3 10
5527 731 31274
5 12
18140 14618 18641 22536 23097
10 23
17236 31594 29094 2412 4316 5044 28515 24737 11578 7907

'''
for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))

    for i in range(M):
        N_list.append(N_list.pop(0))

    print(f'#{tc} {N_list[0]}')