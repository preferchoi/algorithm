ans_list = []
tc = int(input())
for t in range(tc):
    A_P, A_W, B_P, B_W = map(int, input().split(" "))

    A_rate = A_W / A_P
    B_rate = B_W / B_P

    if A_rate > B_rate:
        ans_list.append('BOB')
    elif A_rate < B_rate:
        ans_list.append('ALICE')
    else:
        ans_list.append('DRAW')
n = 1
for i in ans_list:
    print(f'#{n} {i}')
    n += 1