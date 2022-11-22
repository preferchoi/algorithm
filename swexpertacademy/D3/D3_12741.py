ans_list = []

for test_case in range(1,1+int(input())):
    start_A, end_A, start_B, end_B = map(int, input().split(" "))
    # print(start_A, end_A, start_B, end_B)
    start_std, end_std = 0, 0
    if start_A >= start_B:
        start_std = start_A
    else: start_std = start_B
    if end_A >= end_B:
        end_std = end_B
    else: end_std = end_A

    ans = end_std - start_std

    if ans <= 0:
        ans = 0
        ans_list.append(ans)
    else: ans_list.append(ans)
num = 1
for i in ans_list:
    print(f'#{num} {i}')
    num += 1