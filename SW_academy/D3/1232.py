def go(n):
    left, right = tree[n][1], tree[n][2]
    if left:
        go(left)
    if right:
        go(right)
    lst.append(tree[n][0])


for tc in range(1, 11):
    N = int(input())
    tree = [[0, 0, 0] for _ in range(N + 1)]
    for i in range(N):
        node, data, *root = input().split()
        node, root = int(node), list(map(int, root))
        if root:
            tree[node][0] = data
            tree[node][1] = root[0]
            if len(root) == 2:
                tree[node][2] = root[1]
        else:
            tree[node][0] = int(data)

    lst = []
    go(1)

    oper = []
    stack = []
    now = None

    while lst:
        now = lst.pop(0)

        if now not in ['+', '*', '-', '/']:
            stack.append(now)
        else:
            oper = now
            if oper == '+':
                stack.append(stack.pop() + stack.pop())
            elif oper == '*':
                stack.append(stack.pop() * stack.pop())
            elif oper == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif oper == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(b // a)

    print(f'#{tc} {stack.pop()}')
