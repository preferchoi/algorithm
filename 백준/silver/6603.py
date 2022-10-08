def go(tmp):
    if len(tmp) == 6:
        print(*tmp)
        return

    for i in range(N):
        if visited[i]:
            for j in range(i + 1):
                visited[j] = False
            go(tmp + [N_list[i]])
            for j in range(i + 1):
                visited[j] = True


while True:
    N, *N_list = map(int, input().split())
    visited = [True] * N
    if N == 0:
        break

    go([])
    print()
