'''
1
10 9 2 10
1 2 1 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10

13 12 8 13
1 2 1 3 2 4 3 5 3 6 4 7 7 12 5 9 5 8 6 11 6 10 11 13

'''


def order(N):
    global cnt
    cnt += 1
    if tree[N][0]:
        order(tree[N][0])
    if tree[N][1]:
        order(tree[N][1])
    return


for tc in range(1, 1 + int(input())):
    node, way, A, B = map(int, input().split())
    # [left, right, root, num]
    tree = [[0, 0, 0, i] for i in range(node + 1)]

    way_list = list(map(int, input().split()))
    for i in range(0, way * 2, 2):
        if tree[way_list[i]][0]:
            tree[way_list[i]][1] = way_list[i + 1]
        else:
            tree[way_list[i]][0] = way_list[i + 1]
        tree[way_list[i + 1]][2] = way_list[i]

    A_root, B_root = [], []
    while A != 1:
        A_root.append(tree[A][2])
        A = tree[A][2]
    # print(A_root)  # [5, 3, 1]
    while B != 1:
        B_root.append(tree[B][2])
        B = tree[B][2]
    # print(B_root)  # [11, 6, 3, 1]

    same_root = 0
    for i in A_root:
        if i in B_root:
            same_root = i
            break
    # print(same_root)  # 3

    cnt = 0
    order(same_root)

    print(f'#{tc} {same_root} {cnt}')
