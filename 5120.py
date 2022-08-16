'''
3
6 3 3
6 2 4 9 1 5

6 2 4 13 9 1 5
6 2 4 13 9 1 6 5
6 8 2 4 13 9 1 6 5

5 3 5
958 386 329 169 778

958  386  329  498  169  778
958  386  329  498  169  778 1736
958  386  715  329  498  169  778 1736
958  386  715  329  498  667  169  778 1736
958  386  715  329  498  667  169  778 2514  1736
958 1344  386  715  329  498  667  169  778  2514  1736


10 4 10
158  606  636  941  686  774  302  375  954  668



'''


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def print_node_10():
    global head

    node = head
    cnt = -1
    while cnt != 10:
        cnt += 1
        print(node.data, end=' ')
        if node == tail:
            break
        node = node.next
    print()


def insert_list():
    global head
    node = head
    for _ in range(N + K):
        ans_list.append(node.data)
        node = node.next


def lock(M, K):
    global head
    pre_node = head
    node = head.next

    cnt = 0
    for i in range(1, M * K + 1):
        if not i % K:
            new_node = Node(pre_node.data + node.data)
            pre_node.next = new_node
            new_node.next = node
        else:
            pre_node = node
            node = node.next

    return


for tc in range(1, 1 + int(input())):
    N, M, K = map(int, input().split())
    input_list = list(map(int, input().split()))

    head, tail = None, None

    for i in range(1, 1 + N):
        globals()[f'node_{i}'] = Node(input_list[i - 1])

    for i in range(1, N):
        globals()[f'node_{i}'].next = globals()[f'node_{i + 1}']

    head = globals()[f'node_{1}']
    tail = globals()[f'node_{N}']
    tail.next = head

    lock(M, K)

    ans_list = []
    insert_list()

    print(ans_list)

    # cnt = -1
    # print(f'#{tc}', end=' ')
    # for i in range(N + K - 1, -1, -1):
    #     print(ans_list[i], end=' ')
    #     cnt += 1
    #     if cnt > 10:
    #         break
    # print()
