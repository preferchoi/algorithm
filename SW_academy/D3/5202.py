for tc in range(1, 1 + int(input())):
    N = int(input())
    ship_list = [list(map(int, input().split(" "))) for _ in range(N)]
    ship_list.sort()

    count = 0
    end_time = 0
    for i in ship_list:
        if count == 0:
            count += 1
            end_time = i[1]
        if end_time <= i[0]:
            end_time = i[1]
            count += 1
        if end_time > i[0] and end_time > i[1]:
            end_time = i[1]
    print(f'#{tc}', count)
