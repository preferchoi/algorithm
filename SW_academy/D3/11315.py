def go():
    for dy in range(N-4):
        for dx in range(N-4):
            for i in range(5):
                if lst[dy + i][dx + i] == '.':
                    break
            else:
                print('YES')
                return

            for i in range(5):
                if lst[dy + i][dx - i + 4] == '.':
                    break
            else:
                print('YES')
                return

            for x in range(5):
                for y in range(5):
                    if lst[dy + y][dx + x] == '.':
                        break
                else:
                    print('YES')
                    return

            for y in range(5):
                for x in range(5):
                    if lst[dy + y][dx + x] == '.':
                        break
                else:
                    print('YES')
                    return
    print('NO')


for tc in range(1, 1 + int(input())):
    N = int(input())
    lst = [list(input()) for i in range(N)]
    flag = False
    print(f'#{tc}', end=' ')
    go()