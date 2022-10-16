'''
3
1 100
8 5
3 5

'''


def go(n):
    global maxV
    if N - sum(visited) > maxV:
        maxV = N - sum(visited)
    flag = False

    for i in range(N):
        if visited[i] and i != n:
            N_list[n][0] -= N_list[i][1]
            N_list[i][0] -= N_list[n][1]

            if N_list[i][0] <= 0:
                visited[i] = False
            if N_list[n][0] <= 0:
                for next_egg in range(N):
                    if visited[next_egg]:
                        visited[n] = False
                        flag = True
                        go(next_egg)
                        break
            else:
                go(n)

            N_list[n][0] += N_list[i][1]
            N_list[i][0] += N_list[n][1]
            visited[i] = True
            if flag:
                visited[n] = True


N = int(input())
N_list = [list(map(int, input().split())) for _ in range(N)]
visited = [True] * N
maxV = 0
go(0)

print(maxV)