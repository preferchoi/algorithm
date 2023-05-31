
for tc in range(1, 1 + int(input())):
    line = list(0 for _ in range(5000))
    N = int(input())
    for i in range(N):
        Ai, Bi = map(int, input().split())
        for j in range(Ai, Bi + 1):
            line[j] += 1
    P = int(input())
    print(f'#{tc}', end=' ')
    for i in range(P):
        print(line[int(input())], end=' ')
    print()