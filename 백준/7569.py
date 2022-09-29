def BFS(lst):
    global cnt
    flag = True
    for z, x, y in lst:
        for dz, dx, dy in delta:
            ifz, ifx, ify = z + dz, x + dx, y + dy
            if 0 <= ifz < H and 0 <= ifx < M and 0 <= ify < N and visited[ifz][ifx][ify] and base_lst[ifz][ifx][
                ify] == 0:
                base_lst[ifz][ifx][ify] = 1
                flag = False
    if flag:
        return flag
    else:
        return flag


def toma():
    for z in range(H):
        for x in range(M):
            for y in range(N):
                if base_lst[z][x][y] == 0:
                    cnt = 0
                    for dz, dx, dy in delta:
                        ifz, ifx, ify = z + dz, x + dx, y + dy
                        if 0 <= ifz < H and 0 <= ifx < M and 0 <= ify < N and base_lst[ifz][ifx][ify] == -1:
                            cnt += 1
                    if cnt == 6:
                        return False
    return True

delta = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
N, M, H = map(int, input().split())
base_lst = [[list(map(int, input().split())) for _ in range(M)] for _ in range(H)]
visited = [[[True for _ in range(N)] for _ in range(M)] for _ in range(H)]
cnt = 0

flag = toma()

if flag:
    while True:
        tmp = []
        for idx_z in range(H):
            for idx_x in range(M):
                for idx_y in range(N):
                    if base_lst[idx_z][idx_x][idx_y] == 1 and visited[idx_z][idx_x][idx_y]:
                        tmp.append([idx_z, idx_x, idx_y])
                        visited[idx_z][idx_x][idx_y] = False

        if BFS(tmp):
            break
        cnt += 1

    flag = False
    for z in base_lst:
        for y in z:
            for x in y:
                if x == 0:
                    cnt = -1
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
else:
    cnt = -1
print(cnt)
