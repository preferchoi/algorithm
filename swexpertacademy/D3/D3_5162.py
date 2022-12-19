for test in range(1, int(input())+1):
    ABC = list(map(int, input().split()))
    A, B, C = ABC[0], ABC[1], ABC[2]

    # print('현미빵:', A, '단호박빵:', B, '소지자금:', C)
    if A > B:
        F_buy = B
        S_buy = A
    else:
        F_buy = A
        S_buy = B

    count = 0
    while True:
        count += 1
        if F_buy * count > C:
            count -= 1
            if F_buy*count - C >= S_buy:
                count +=1
            break

    print(f'#{test}', count)