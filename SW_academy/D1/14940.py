def find():
    for y in range(N):
        for x in range(N - M + 1):
            if s_list[y][x:x + M - 1] == s_list[y][x + M - 1:x:-1]:
                return ''.join(s_list[y][x:x + M])

            y_list = []
            for m in range(M):
                y_list.append(s_list[x+m][y])

            if y_list == y_list[::-1]:
                return ''.join(y_list)

for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    s_list = [list(input()) for _ in range(N)]

    print(f'#{tc} {find()}')