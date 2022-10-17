from collections import deque

N, M = map(int, input().split())
# N, M = 7, 3
base = deque(range(1, N + 1))

print('<', end='')
while base:
    for i in range(M - 1):
        base.append(base.popleft())
    print(base.popleft(), end='')
    if not base:
        break
    print(',', end=' ')
print('>')
