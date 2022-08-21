def push(x):  # 정수 X를 큐에 넣는 연산이다.
    queue.append(x)
    return


def pop():  # 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if not queue:
        print(-1)
        return
    else:
        print(queue.pop(0))
        return


def size():  # 큐에 들어있는 정수의 개수를 출력한다.
    print(len(queue))
    return


def empty():  # 큐가 비어있으면 1, 아니면 0을 출력한다.
    if queue:
        print(0)
        return
    else:
        print(1)
        return


def front():  # 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if queue:
        print(queue[0])
        return
    else:
        print(-1)
        return


def back():  # 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if queue:
        print(queue[-1])
        return
    else:
        print(-1)
        return


queue = []
N = int(input())

for _ in range(N):
    for i in input().split():
        if len(i) == 1:
            push(int(i))
        elif i == 'pop':
            pop()
        elif i == 'size':
            size()
        elif i == 'empty':
            empty()
        elif i == 'front':
            front()
        elif i == 'back':
            back()


