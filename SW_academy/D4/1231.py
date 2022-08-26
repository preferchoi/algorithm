def ino(root):
    if tree[root][0] != 0:
        ino(tree[root][0])
    print(data[root], end='')
    if tree[root][1] != 0:
        ino(tree[root][1])


for tc in range(1, 11):
    V = int(input())
    tree = [[0, 0] for _ in range(V + 1)]
    data = [0] * (V + 1)
    for _ in range(V):
        a, b, *c = input().split()
        a, c = int(a), list(map(int, c))
        data[a] = b
        if len(c) == 2:
            tree[a] = c
        elif len(c) == 1:
            tree[a][0] = c[0]

    print(f'#{tc}', end=' ')
    ino(1)
    print()

'''
8
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S

'''
