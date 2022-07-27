for test in range(10):
    N = input()

    array = []
    # 리스트 받아오기
    for i in range(100):
        ary = input().split(" ")
        ary.pop(len(ary)-1)
        ary = list(map(int, ary))
        array.append(ary)

    M = 0
    # 우하향
    S = 0
    for i in range(100):
        S += array[i][i]
    if M < S:
        M = S
    # 좌하향
    S = 0
    for i in range(100):
        S += array[i][99-i]
    if M < S:
        M = S

    # 가로
    for i in range(100):
        S = 0
        for j in range(100):
            S += array[i][j]
        if M < S:
            M = S
    
    # 세로
    for i in range(100):
        S = 0
        for j in range(100):
            S += array[j][i]
        if M < S:
            M = S

    print(f'#{N}', M)