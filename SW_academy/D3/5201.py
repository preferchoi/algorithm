for test in range(int(input())):
    N, M = map(int, input().split(" "))
    N_w = list(map(int, input().split(" ")))  # 화물무게
    M_w = list(map(int, input().split(" ")))  # 트럭무게
    N_w.sort(reverse=True)
    M_w.sort(reverse=True)
    x, ans = 0, 0

    for i in M_w:
        for j in range(x, len(N_w)):
            if N_w[j] <= i:
                x += 1
                ans += N_w[j]
                break
            else:
                x += 1
    print(f'#{test + 1}', ans)
