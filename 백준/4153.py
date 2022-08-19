while True:
    N_list = list(map(int, input().split()))
    N_list.sort()
    a, b, c = N_list[0], N_list[1], N_list[2]
    if not a and not b and not c:
        break
    if c ** 2 == a ** 2 + b ** 2:
        print('right')
    else:
        print('wrong')
