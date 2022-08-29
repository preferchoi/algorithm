x_last, y_last = map(int, input().split())
x_lst, y_lst = [0, x_last], [0, y_last]

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    if x == 1:
        x_lst.append(y)
    else:
        y_lst.append(y)
x_lst.sort()
y_lst.sort()

cnt_x, cnt_y = 0, 0
pre = 0
for i in x_lst:
    if i - pre > cnt_x:
        cnt_x = i - pre
    pre = i
pre = 0
for i in y_lst:
    if i - pre > cnt_y:
        cnt_y = i - pre
    pre = i

print(cnt_x * cnt_y)
