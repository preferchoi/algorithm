'''
9 9
4 1 1 2 2 3 2 7 5 6 7 6 1 5 8 5 8 9
5 4
1 2 2 3 4 1 1 5
'''

for tc in range(1, 11):
    V, E = map(int, input().split())
    tree = [[] for _ in range(V + 1)]
    order = list(map(int, input().split()))
    for i in range(0, E * 2, 2):
        tree[order[i + 1]].append(order[i])
    print(tree)

    while True:
        for i in range(1, V + 1):
            if not tree[i]:
