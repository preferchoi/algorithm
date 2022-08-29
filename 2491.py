N = int(input())
N_list = list(map(int, input().split()))
pre, cnt, maxV = 0, 1, 1

for i in N_list[1:]:
    if pre <= i:
        cnt += 1
    else:
        if cnt > maxV:
            maxV = cnt
        cnt = 1
    pre = i
pre = 999
cnt = 1
for i in N_list[1:]:
    if pre >= i:
        cnt += 1
    else:
        if cnt > maxV:
            maxV = cnt
        cnt = 1
    pre = i
print(maxV)
