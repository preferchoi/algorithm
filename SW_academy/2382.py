delta = [[0, 1], [-1, 0], [1, 0], [0, -1]]
for tc in range(1, 1 + int(input())):
    # n*n 배열, m초, K 군집 수
    N, M, K = map(int, input().split())
    # 미생물 군집
    # x, y, 거주민 수, 이동방향
    # 이동방향은 %4로 처리해서 4를 0으로 바꿔줌
    lst = [list(map(int, input().split())) for _ in range(K)]
    print(lst)
    cnt = 0

    while cnt <= M:
        cnt += 1
        for i in range(len(lst)):
            go = delta[lst[i][3] % 4]
            dx, dy = lst[i][0] + go[0], lst[i][1] + go[1]
            if 0 <= dx < N and 0 <= dy < N:
                lst[i][0] = dx
                lst[i][1] = dy
            else:
                lst[i][3] = (lst[i][3] + 2) % 4
    print(lst)
    '''
    M이 2N 이하일 때 = 하나씩 차근차근 돌린다
    M이 2N 이상일 때, 벽에 붙이고 (남은 M초 // N)만큼 2로 나눠줌
    미생물군집은 줄어들 수 있음
    '''

'''
k개 처리

'''