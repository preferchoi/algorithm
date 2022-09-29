def bfs(idx, sumV):
    global ans

    if ans < sumV:
        return

    if idx >= cnt:
        ans = sumV
        return

    bat = lst[idx]
    for i in range(bat, 0, -1):
        bfs(idx + i, sumV + 1)


for tc in range(1, 1 + int(input())):
    ans = 10**10
    lst = list(map(int, input().split()))
    cnt = lst.pop(0) - 1

    bfs(0, -1)
    print(f'#{tc} {ans}')
