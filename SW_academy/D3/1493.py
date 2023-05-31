cnt = 1
n_list = []
while cnt < 284:
    for i in range(cnt):
        n_list.append([cnt - i, i + 1])
    cnt += 1

for tc in range(1, 1 + int(input())):
    A, B = map(int, input().split())
    print(f'#{tc} {n_list.index([n_list[A - 1][0] + n_list[B - 1][0], n_list[A - 1][1] + n_list[B - 1][1]]) + 1}')
