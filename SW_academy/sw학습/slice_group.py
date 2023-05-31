from collections import deque
'''
3
5 2
1 2 3 4
5 3
1 2 2 3 4 5
7 4
2 3 4 5 4 6 7 4

'''
def oper():

    while Q:
        A, B = Q.popleft()
        graph[A-1], graph[B-1] = graph[B-1], graph[A-1]
    return


for tc in range(1, int(input())+ 1):

    N, M = map(int, input().split())
    setup = list(map(int, input().split()))
    Q = deque()

    for i in range(0, M*2, 2):
        Q.append(sorted([setup[i], setup[i+1]]))

    graph = []
    for i in range(N):
        graph.append(i+1)

    print(Q)
    oper()
    print(graph)
    ans = set(graph)
    print(ans)
    print(len(ans))
