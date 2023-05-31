for test in range(1, int(input())+1):
    S = list(input())
    L_count = 0
    for i in S:
        S_count = 0
        for j in S:
            if i == j:
                S_count += 1
        if S_count == 2:
            L_count += 1
    if L_count == 4:
        print(f'#{test}', 'Yes')
    else:
        print(f'#{test}', 'No')