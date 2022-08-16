class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def print_list():
    global main_head
    node = main_head
    while node:
        print(node.data)
        node = node.next
    print()


def print_back_10():
    global main_head
    node = main_head
    cnt = -1
    while node:
        cnt += 1
        if cnt > N * M - 11:
            back_10.append(node.data)
        node = node.next


def change_idx():
    global main_head, main_tail, new_head, new_tail
    if main_head.data > new_head.data:
        new_tail.next = main_head
        main_head = new_head
        return

    node = main_head
    while node:
        if not node.next:
            main_tail.next = new_head
            return
        if node.next.data and node.next.data > new_head.data:
            new_tail.next = node.next
            node.next = new_head
            return
        node = node.next


for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    main_head, main_tail = None, None
    setting = list(map(int, input().split()))

    for i in range(1, N + 1):
        globals()[f'node_{i}'] = Node(setting[i - 1])

    for i in range(1, N):
        globals()[f'node_{i}'].next = globals()[f'node_{i + 1}']
    main_head, main_tail = globals()[f'node_{1}'], globals()[f'node_{N}']

    for _ in range(M - 1):
        setting = list(map(int, input().split()))
        new_head, new_tail = None, None

        for i in range(1, N + 1):
            globals()[f'new_node_{i}'] = Node(setting[i - 1])

        for i in range(1, N):
            globals()[f'new_node_{i}'].next = globals()[f'new_node_{i + 1}']
        new_head, new_tail = globals()[f'new_node_{1}'], globals()[f'new_node_{N}']

        change_idx()
    back_10 = []
    print_back_10()
    back_10.reverse()
    print(f'#{tc}', end=' ')
    print(*back_10)

