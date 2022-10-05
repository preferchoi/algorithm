import heapq

V, E = map(int, input().split())
INF = 10 * V + 1
tree = [[] for _ in range(V + 1)]
K = int(input())
for i in range(E):
    u, v, w = map(int, input().split())
    tree[u] += [[v, w]]

# 출발 노드부터 각각의 노드까지 가는 비용의 최소 합 구할 요량으로 만듬
ans = [INF] * (V + 1)
# 갈 수 있는 노드 임시저장용
q = []
# 본인은 어짜피 그 자리니까 비용 0
ans[K] = 0
# q에 비용과 시작 노드 위치 넣어줌
heapq.heappush(q, (0, K))

while q:
    dist, now_node = heapq.heappop(q)
    for n, weight in tree[now_node]:
        cost = dist + weight
        # 비용을 이전 보다 적게 썼으면 현재 이동한 경로로 바꿔줌
        if cost < ans[n]:
            ans[n] = cost
            heapq.heappush(q, (cost, n))

for i in ans[1:]:
    if i == INF:
        print('INF')
    else:
        print(i)
