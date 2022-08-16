'''
1
5 2 5
1 2 3 4 5
2 7
4 8

'''


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def insert_node(idx, data):
    global head

    new_node = Node(data)
    node_P = head
    node_T = head

    if idx == 0:
        new_node.next = head
        head = new_node
        return

    now_idx = 0
    while idx != now_idx:
        node_P = node_T
        node_T = node_T.next
        now_idx += 1
    new_node.next = node_T
    node_P.next = new_node


def print_list():
    global head
    node = head
    while node:
        print(node.data)
        node = node.next
    print()


def print_select(tc, idx):
    global head
    node = head
    for _ in range(idx):
        node = node.next
    print(f'#{tc} {node.data}')


for tc in range(1, 1 + int(input())):
    N, M, L = map(int, input().split())
    N_list = list(map(int, input().split()))
    head = None
    # 노드 생성
    for i in range(1, 1 + N):
        globals()[f'node_{i}'] = Node()

    # 노드 데이터 삽입
    for i in range(1, 1 + N):
        globals()[f'node_{i}'].data = N_list[i - 1]

    # 노드 다음 리스트 지정
    for i in range(1, N):
        globals()[f'node_{i}'].next = globals()[f'node_{i + 1}']

    head = node_1

    for _ in range(M):
        plus_idx, new_value = map(int, input().split())
        insert_node(plus_idx, new_value)

    print_list()
    print_select(tc, L)
