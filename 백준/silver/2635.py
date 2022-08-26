N = int(input())
maxV = 0
maxK = 0
max_list = []
for i in range(N + 1):
    tmp = [N, i]
    key = 0
    cnt = 0
    while key >= 0:
        key = tmp[cnt] - tmp[cnt + 1]
        tmp.append(key)
        cnt += 1
    else:
        tmp.pop()
    if maxV < len(tmp):
        maxK = i
        maxV = len(tmp)
        max_list = tmp[:]
print(maxV)
print(*max_list)
