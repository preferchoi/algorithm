def go(y, x, cnt, change_go, runaway):
    if change_go == 3 and y == go_y and x == go_x:
        global ans
        if ans < len(cnt):
            ans = len(cnt)
        return
    if 4 <= change_go:
        return
    for dy, dx in delta[change_go], delta[(change_go + 1) % 4]:
        ify, ifx = y + dy, x + dx

        if 0 <= ifx < N and 0 <= ify < N:
            tmp = lst[ify][ifx]
            if tmp not in cnt:
                if runaway == (dy, dx):
                    go(ify, ifx, cnt + [tmp], change_go, runaway)
                else:
                    go(ify, ifx, cnt + [tmp], change_go + 1, (dy, dx))


delta = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
for tc in range(1, 1 + int(input())):
    N = int(input())
    lst = [input().split() for _ in range(N)]
    # print(lst)

    # 현재 좌표, 메뉴 체크용, 방향 전환 수, 현재 진행 방향
    ans = 0
    for go_y in range(N):
        for go_x in range(N):
            go(go_y, go_x, [], 0, delta[0])

    print(f'#{tc}', end=' ')
    if ans:
        print(ans)
    else:
        print(-1)

'''
진행 방향 체크, 3번 꺾었고 제자리 복귀 = 끝
재방문, 동일 메뉴 = 끝
재방문 = 동일 메뉴, 하나는 생각 안해도 됨
사각형 모서리가 항상 맨 위에 있게
시작점이 오른쪽, 왼쪽, 아래쪽에 있으면
어짜피 중복이거든 
'''
