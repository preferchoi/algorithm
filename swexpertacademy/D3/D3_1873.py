'''
1
3 7
***....
*-..#**
#<.****
23
SURSSSSUSLSRSSSURRDSRDS
3 7
***....
*-..#**
#<.****
23
SURSSSSUSLSRSSSURRDSRDS

'''
for tc in range(1, 1 + int(input())):
    H, W = map(int, input().split())
    mapping = []
    for i in range(H):
        mapping.append(list(input()))
    N = int(input())
    setting = list(input())
    tank_H, tank_W = 0, 0
    for i in range(H):
        for j in range(W):
            if mapping[i][j] in ['<', '>', '^', 'v']:
                tank_H, tank_W = i, j
    # print(tank_H, tank_W)

    for i in setting:
        if i == 'U':
            mapping[tank_H][tank_W] = '^'
            if tank_H == 0:
                pass
            elif mapping[tank_H - 1][tank_W] == '.':
                mapping[tank_H][tank_W] = '.'
                mapping[tank_H - 1][tank_W] = '^'
                tank_H -= 1

        elif i == 'D':
            mapping[tank_H][tank_W] = 'v'
            if tank_H == H-1:
                pass
            elif mapping[tank_H + 1][tank_W] == '.':
                mapping[tank_H][tank_W] = '.'
                mapping[tank_H + 1][tank_W] = 'v'
                tank_H += 1

        elif i == 'L':
            mapping[tank_H][tank_W] = '<'
            if tank_W == 0:
                pass
            elif mapping[tank_H][tank_W-1] == '.':
                mapping[tank_H][tank_W] = '.'
                mapping[tank_H][tank_W-1] = '<'
                tank_W -= 1

        elif i == 'R':
            mapping[tank_H][tank_W] = '>'
            if tank_W == W-1:
                pass
            elif mapping[tank_H][tank_W+1] == '.':
                mapping[tank_H][tank_W] = '.'
                mapping[tank_H][tank_W+1] = '>'
                tank_W += 1

        elif i == 'S':
            if mapping[tank_H][tank_W] == '<':
                for c in range(tank_W, -1, -1):
                    if mapping[tank_H][c] in ['*', '#']:
                        if mapping[tank_H][c] == '*':
                            mapping[tank_H][c] = '.'
                        break
            elif mapping[tank_H][tank_W] == '>':
                for c in range(tank_W, W):
                    if mapping[tank_H][c] in ['*', '#']:
                        if mapping[tank_H][c] == '*':
                            mapping[tank_H][c] = '.'
                        break
            elif mapping[tank_H][tank_W] == '^':
                for c in range(tank_H, -1, -1):
                    if mapping[c][tank_W] in ['*', '#']:
                        if mapping[c][tank_W] == '*':
                            mapping[c][tank_W] = '.'
                        break
            elif mapping[tank_H][tank_W] == 'v':
                for c in range(tank_H, H):
                    if mapping[c][tank_W] in ['*', '#']:
                        if mapping[c][tank_W] == '*':
                            mapping[c][tank_W] = '.'
                        break
        # print(i, tank_H, tank_W)
        # print(mapping[0])
        # print(mapping[1])
        # print(mapping[2])
    print(f'#{tc} ', end='')
    for i in range(H):
        for j in range(W):
            print(mapping[i][j], end='')
        print()