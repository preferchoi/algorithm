N, M = map(int, input().split())
N_list = [[0, 0] for _ in range(6)]
for i in range(N):
    s, g = map(int, input().split())
    N_list[g-1][s] += 1

cnt = 0
for i, j in N_list:
    if i % M:
        cnt += i//M + 1
    else:
        cnt += i//M
    if j % M:
        cnt += j//M + 1
    else:
        cnt += j//M

print(cnt)