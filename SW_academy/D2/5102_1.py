'''
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
1 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9

'''
for tc in range(1, 1 + int(input())):
    node, road = map(int, input().split())
    nodes = [[] for _ in range(node + 1)]
    visited = [True for _ in range(node + 1)]
    for _ in range(road):
        s, e = map(int, input().split())
        nodes[s].append(e)
        nodes[e].append(s)
    start, end = map(int, input().split())
    queue = [[start, -1]]

    while queue:
        start, deep = queue.pop(0)
        deep += 1
        for i in nodes[start]:
            if visited[i]:
                visited[i] = False
                queue.append([i, deep])
        if start == end:
            break
    else:
        deep = 0

    print(f'#{tc} {deep}')
