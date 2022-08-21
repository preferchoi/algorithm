N = int(input())
N_list = [list(map(int, input().split())) for _ in range(N)]
idx_list = [0 for _ in range(N)]

for i in range(N):
    cnt = 1
    for w, h in N_list:
        if N_list[i][0] < w and N_list[i][1] < h:
            cnt += 1
    idx_list[i] = cnt
print(*idx_list)