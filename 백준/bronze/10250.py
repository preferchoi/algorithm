for tc in range(1, 1 + int(input())):
    H, W, num = map(int, input().split())

    cnt = 0
    flag = 0
    for y in range(1, W + 1):
        for x in range(1, H + 1):
            cnt += 1
            if cnt == num:
                if y < 10:
                    print(f'{x}0{y}')
                else:
                    print(f'{x}{y}')
                flag = 1
                break
        if flag:
            break
