'''
4
SLSSLLSSRS
LS
S
LLLLC

'''

dx = [1, 0, -1, 0]
dy = [0, -1, 0, -1]

for tc in range(1, 1 + int(input())):
    s_list = list(input())
    point = [0, 0]
    go = 0
    maxi = 0
    for i in s_list:
        if i == 'S':
            point = [point[0] + dx[go], point[1] + dy[go]]
            if maxi < abs(point[0]) + abs(point[1]):
                maxi = abs(point[0]) + abs(point[1])
        elif i == 'L':
            go = (go + 1) % 4
        elif i == 'R':
            go = (4 + go - 1) % 4

    print(maxi, go, point)

    print(f'#{tc} {maxi}')































    # if point == [0, 0]: # 원점에 있을 때
    #     print(f'#{tc} {maxi}')
    # else:
    #     if point[0] > 0:
    #         if go == 0:
    #             print(f'#{tc} oo')
    #         elif go == 2:
    #             print(f'#{tc} {maxi}')
    #         else:
    #             if abs(point[0]) + abs(point[1]) > maxi:
    #                 print(f'#{tc} {abs(point[0]) + abs(point[1])}')
    #             else:
    #                 print(f'#{tc} {maxi}')
    #     elif point[0] < 0:
    #         if go == 2:
    #             print(f'#{tc} oo')
    #         elif go == 0:
    #             print(f'#{tc} {maxi}')
    #         else:
    #             if abs(point[0]) + abs(point[1])> maxi:
    #                 print(f'#{tc} {abs(point[0]) + abs(point[1])}')
    #             else:
    #                 print(f'#{tc} {maxi}')
    #     elif point[1] < 0:
    #         if go == 1:
    #             print(f'#{tc} oo')
    #         elif go == 3:
    #             print(f'#{tc} {maxi}')
    #         else:
    #             if abs(point[0]) + abs(point[1]) > maxi:
    #                 print(f'#{tc} {abs(point[0]) + abs(point[1])}')
    #             else:
    #                 print(f'#{tc} {maxi}')
    #     elif point[1] < 0:
    #         if go == 3:
    #             print(f'#{tc} oo')
    #         elif go == 1:
    #             print(f'#{tc} {maxi}')
    #         else:
    #             if abs(point[0]) + abs(point[1]) > maxi:
    #                 print(f'#{tc} {abs(point[0]) + abs(point[1])}')
    #             else:
    #                 print(f'#{tc} {maxi}')
