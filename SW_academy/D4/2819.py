def go(y, x, cnt):
    if len(cnt) == 7:
        tmp.add(cnt)
        return
    for dy, dx in delta:
        ify, ifx = y + dy, x + dx
        if 0 <= ifx < 4 and 0 <= ify < 4:
            go(ify, ifx, cnt + lst[ify][ifx])


for tc in range(1, 1 + int(input())):
    lst = [input().split() for _ in range(4)]
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    tmp = set()
    for Y in range(4):
        for X in range(4):
            go(Y, X, '')
    print(f'#{tc} {len(tmp)}')
