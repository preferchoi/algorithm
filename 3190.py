from collections import deque

N = int(input())
base_lst = [list(0 for _ in range(N)) for _ in range(N)]

apple_N = int(input())
for _ in range(apple_N):
    x, y = map(int, input().split())
    base_lst[x-1][y-1] = 1
oper_N = int(input())
oper = deque([])
for _ in range(oper_N):
    t, op = input().split()
    if op == 'D':
        op = 1
    else:
        op = -1
    oper += [[int(t), op]]

cnt = 0
snake = deque([[0, 0]])
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
head_y, head_x, head = 0, 0, 0
time, op = oper.popleft()

while True:
    cnt += 1
    head_y += delta[head][0]
    head_x += delta[head][1]
    if not 0 <= head_x < N or not 0 <= head_y < N:
        break
    if [head_y, head_x] in snake:
        break
    snake.append([head_y, head_x])
    if base_lst[head_y][head_x]:
        base_lst[head_y][head_x] = 0
    else:
        snake.popleft()
    if cnt == time:
        head += op
        head %= 4
        if oper:
            time, op = oper.popleft()

print(cnt)
