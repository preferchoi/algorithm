# for tc in range(1, 11):

N = int(input())
N_list = []
for i in range(100):
    N_list.append(list(map(int, input().split())))
visit_list = [[False for _ in range(100)] for _ in range(100)]
now_x = -1
now_y = 99
for i in N_list[-1]:
    now_x += 1
    if i == 2:
        break

print(now_x)

go_y = [0, 0, -1]
go_x = [-1, 1, 0]

while now_y != 0:
    for i in range(3):
        dy = now_y + go_y[i]
        dx = now_x + go_x[i]

        if 0 <= dy <= 99 and visit_list[dy][dx]:
            
