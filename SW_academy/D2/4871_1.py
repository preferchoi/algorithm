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
2 5
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
    V, E = map(int, input().split())
    node_list = [[] for _ in range(V + 1)]
    visited = [True for _ in range(V + 1)]

    for i in range(E):
        start, end = map(int, input().split())
        node_list[start].append(end)

    start, end = map(int, input().split())
    stack = [start]
    print(f'#{tc}', end=' ')
    while start != end:
        if not stack:
            print(0)
            break
        start = stack.pop()

        if visited[start]:
            visited[start] = False
        else:
            continue

        for i in node_list[start]:
            stack.append(i)
    else:
        print(1)
