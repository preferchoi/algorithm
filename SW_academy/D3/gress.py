for test in range(1, int(input())+1):
    N = int(input())
    G = []
    for i in range(N):
        G.append(int(input()))

    s = 0
    for i in G:
        s += i
    A = [s/N] * N

    P = 0
    for i in range(N):
        a = G[i] - A[i]
        if a > 0:
            P += a
    print(f'#{test}', int(P))