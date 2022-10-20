T = int(input())

for i in range(1, T+1):
    time = input().split(" ")
    F_h, F_m, S_h, S_m = int(time[0]), int(time[1]), int(time[2]), int(time[3])
    # print('F_h:', F_h, 'F_m:', F_m, 'S_h:', S_h, 'S_m:', S_m)
    T_h = F_h + S_h
    T_m = F_m + S_m
    if T_m > 60:
        T_h += 1
        T_m -= 60
    if T_h > 12:
        T_h -= 12
    print(f'#{i}', T_h, T_m)