for tc in range(1, 1+ int(input())):
    game = list(input())
    # print(game)

    x_count = 0
    o_count = 0

    result = 'YES'

    for i in game:
        if i == 'x':
            x_count += 1
        if i == 'o':
            o_count += 1
    if 15 - x_count < 8:
        result = 'NO'
    print(f'#{tc} {result}')