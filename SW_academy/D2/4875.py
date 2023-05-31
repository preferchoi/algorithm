'''
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000

'''
from pprint import pprint

TC = int(input())
for tc in range(1, 1 + TC):
    N = int(input())
    N_list = [list(map(int, input())) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    result = 0  # 결과 출력용 변수
    stack = []  # 여기에다 경우의 수 집어넣을거임

    # 첫 시작점, 2 찾아서 스택에 집어넣음
    for qy in range(N):
        for qx in range(N):
            if N_list[qy][qx] == 2:
                stack.append([qy, qx])

    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    # 도착한다는 결과가 나올 수 있으면 while문 멈추게 했음
    while not result:
        # 스택이 비어있으면 브레이크, IndexError 대신해서 넣음
        # 맨 처음 돌릴 때는 2 위치 있어서 안터짐 그 다음엔 갈 수 있는데 없으면 터짐
        if not stack:
            break
        # 스택에서 갈 수 있는 곳 y, x 값 지정
        y, x = stack.pop()

        # 상하좌우 다 봐야하니까 델타 이용해서 4번 반복
        for i in range(4):
            ify = y + dy[i]
            ifx = x + dx[i]

            # 리스트 범위 내부에 위치했는지, 방문한 지역인지 확인
            if 0 <= ify < N and 0 <= ifx < N and not visited[ify][ifx]:
                # 만약 갈 수 있는 곳이다? 스택에 추가해 주고 방문 체크
                if N_list[ify][ifx] == 0:
                    stack.append([ify, ifx])
                    visited[ify][ifx] = True
                # 만약 도착지다? 맨 겉 while문 탈출조건 맞춰주고 break
                if N_list[ify][ifx] == 3:
                    result = 1
                    break

    print(f'#{tc} {result}')
