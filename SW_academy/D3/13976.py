'''
1
9
XXXXXXXXX
XXXHXXXXX
XXHAHXXHX
XXHHXXXXX
XXXXXXXXX
XXAHHXXXX
XXHXXHAHX
XXAHXXHXX
XXHXHXXXX
XXXXXXXXX

'''
for tc in range(1, 1 + int(input())):
    N = int(input())
    N_list = [list(input()) for _ in range(N + 1)]
    # A, B, C
    for y in range(N + 1):
        for x in range(N):
            flag = 0
            if N_list[y][x] == 'X':
                N_list[y][x] = 0
            elif N_list[y][x] == 'A':
                flag = 1
            elif N_list[y][x] == 'B':
                flag = 2
            elif N_list[y][x] == 'C':
                flag = 3
            if flag:
                for yx in range(-flag, flag + 1):
                    if 0 <= y + yx < N + 1:
                        if N_list[y + yx][x] == 'H':
                            N_list[y + yx][x] = 0
                    if 0 <= x + yx < N:
                        if N_list[y][x + yx] == 'H':
                            N_list[y][x + yx] = 0

    cnt = 0
    for y in range(N + 1):
        for x in range(N):
            if N_list[y][x] == 'H':
                N_list[y][x] = 1
                cnt += 1
    print(f'#{tc} {cnt}')
