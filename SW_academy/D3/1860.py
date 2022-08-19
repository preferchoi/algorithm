for tc in range(1, 1 + int(input())):
    N, M, K = map(int, input().split())
    N_list = list(map(int, input().split()))
    save = 0
    time_laps = [0 for _ in range(max(N_list) + 1)]

    for i in N_list:
        time_laps[i] += 1
    # print(time_laps)
    print(f'#{tc}', end=' ')
    if sum(time_laps[:M]):
        print('Impossible')
        continue

    for i in range(M, len(time_laps)):
        if not i % M:
            save += K
        save -= time_laps[i]
        if save < 0:
            print('Impossible')
            break
    else:
        print('Possible')
