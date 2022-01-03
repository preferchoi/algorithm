for test in range(1, int(input())+1):
    pq = list(map(float, input().split(" ")))
    p, q = pq[0], pq[1]

    if p * (1-q) * q > (1-p) * q:
        print(f'#{test} YES')
    else:
        print(f'#{test} NO')