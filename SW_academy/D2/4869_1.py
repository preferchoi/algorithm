ans_list = [0, 1, 3]
for i in range(3, 31):
    ans_list.append(ans_list[i-1] + 2 * ans_list[i-2])

for tc in range(1, 1 + int(input())):
    N = int(input())
    print(f'#{tc} {ans_list[N // 10]}')
