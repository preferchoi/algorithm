class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def yose(c):
    global head
    node = head
    cnt = 1
    print('<', end='')
    while node:
        cnt += 1
        if cnt == c:
            print(node.next.data, end=', ')
            node.next = node.next.next
            cnt = 1
            if node == node.next:
                print(node.data, end='')
                print('>')
                break
        node = node.next


N, M = map(int, input().split())
head = Node(1)
pre = head
for i in range(2, N + 1):
    node = Node(i)
    pre.next = node
    pre = node
pre.next = head

yose(M)

'''
1 2 3 4 5 6 7
1 2 4 5 7


3 6 2 7 5 1 4
'''
