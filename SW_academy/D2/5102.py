from pprint import pprint
for tc in range(1, 1 + int(input())):
    V, E = map(int, input().split())
    map_list = [[False for _ in range(V+1)] for _ in range(V+1)]
    queue = []
    deep = -1

    for _ in range(E):
        s1, s2 = map(int, input().split())
        map_list[s1][s2] = True
        map_list[s2][s1] = True

    q_start, q_end = map(int, input().split())
    queue.append([q_start, deep])
    # pprint(map_list)
    while queue:
        q_start, deep = queue.pop(0)
        deep += 1

        if q_start == q_end:
            break

        for i in range(V+1):
            if  map_list[q_start][i]:
                map_list[q_start][i] = False
                queue.append([i, deep])
    else:
        deep = 0
    print(f'#{tc} {deep}')
