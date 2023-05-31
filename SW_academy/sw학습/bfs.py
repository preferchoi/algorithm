from collections import deque

'''
def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
        return visited


graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1

print(BFS_with_adj_list(graph_list, root_node))
'''


def oper():

    global result

    while Q:
        front, check = Q.popleft()
        if front == M:
            result = check
            return

        for i in range(4):
            if i == 0:
                if 1 <= front + 1 <= 1000000 and not visited[front + 1]:
                    Q.append([front + 1, check + 1])
                    visited[front + 1] = True
            elif i == 1:
                if 1 <= front - 1 <= 1000000 and not visited[front - 1]:
                    Q.append([front - 1, check + 1])
                    visited[front - 1] = True
            elif i == 2:
                if 1 <= front * 2 <= 1000000 and not visited[front * 2]:
                    Q.append([front * 2, check + 1])
                    visited[front * 2] = True
            elif i == 3:
                if 1 <= front - 10 <= 1000000 and not visited[front - 10]:
                    Q.append([front - 10, check + 1])
                    visited[front - 10] = True


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = 0
    visited = [False] * 10000001
    Q = deque()
    Q.append((N, 0))
    oper()

    print(f'#{tc} {result}')
'''
방문 했는지 안했는지 판단?
3
2 7
3 15
36 1007

'''
