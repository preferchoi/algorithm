T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    list = []
    for i in range(N):
        list.append(input().split(" "))
    # print(list)

    N_speed = 0
    T_len = 0

    for i in range(N):
        # 어짜피 속도변화 없으니 걍 바로 더하면 되는거였음
        # if list[i][0] == '0':
        #     continue
        if list[i][0] == '1':
            N_speed += int(list[i][1])
        if list[i][0] == '2':
            N_speed -= int(list[i][1])

        if N_speed < 0:
            N_speed = 0

        T_len += N_speed

    print(f'#{test_case}', T_len)