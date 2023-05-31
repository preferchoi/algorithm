for tc in range(1, 1 + int(input())):
    AB = list(map(int, input().split(" ")))
    A = [0 for _ in range(10)]
    B = [0 for _ in range(10)]
    turn = 0
    ans_print = True
    win = False
    flag = True
    tmp = None
    print(f'#{tc}', end=' ')
    for i in AB:
        if flag:
            A[i] += 1
            tmp = A
            flag = False
        else:
            B[i] += 1
            tmp = B
            flag = True
        if 3 in tmp:
            win = True

        for j in range(8):
            if tmp[j] and tmp[j + 1] and tmp[j + 2]:
                win = True

        if win:
            if flag:
                print('2')
            else:
                print('1')
            break
    else:
        print('0')
