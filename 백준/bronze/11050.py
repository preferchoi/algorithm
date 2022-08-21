# from itertools import combinations
#
# N, M = map(int, input().split())
#
# print(len(list(combinations(range(N), M))))

N, M = map(int, input().split())

key = 1 << N
cnt = 0
for i in range(1 << N):
    arr = []
    for j in range(N):
        if i & (1 << j):
            arr.append(j)

    if len(arr) == M:
        print(arr)
        cnt += 1
print(cnt)
