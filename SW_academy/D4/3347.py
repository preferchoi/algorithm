'''
2
4 3
5 3 1 4
4 3 2
6 6
3 1 4 1 5 9
2 6 5 3 5 9

'''
for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    N_idx = [0 for _ in range(N)]
    M_list = list(map(int, input().split()))

    for m in M_list:
        for n in range(N):
            if N_list[n] <= m:
                N_idx[n] += 1
                break
    print(f'#{tc} {N_idx.index(max(N_idx))+1}')
