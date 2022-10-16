'''
2
2 3
10 10

'''

for tc in range(1, 1 + int(input())):
    R, C = map(int, input().split())
    if R > C:
        key = C
    else:
        key = R
    cnt = 0
    cnt_2 = 0
    while R and C:
        cnt += 4 * R * C - 2 * R - 2 * C + 1
        cnt_2 += 6*R*C-4*R-4*C+4
        R -= 1
        C -= 1
    print(cnt_2)
    x, y = cnt // 2 + key // 2, cnt // 2 - key // 2
    print(x, y)
'''
4 * X * Y - 2 * (X + Y) + 1 + 4 * (X - 1) * (Y - 1) - 2 * ((X - 1) * (Y - 1)) + 1
4 * X * Y - 2 * (X + Y) + 1 + 4(XY - X - Y + 1) - 2 (XY - X - Y + 1) + 1
4XY - 2X - 2Y + 1 + 4XY - 4X - 4Y + 4 - 2XY + 2X + 2Y - 2 + 1
6XY - 4X - 4Y + 4
 



cnt = X * Y + (X - 1) * (Y - 1)
cnt_2 = X * (Y - 1) + (X - 1) * Y
cnt + cnt_2 = X * Y + (X - 1) * (Y - 1) + X * (Y - 1) + (X - 1) * Y
            = ([X * Y]) + ([X * Y] - X - Y + 1) + ([X * Y] - X) + ([X * Y] - Y)
            = 4 * X * Y - (X + Y + 1) - X - Y
            = 4 * X * Y - 2 * X - 2 * Y + 1
            

 
'''
