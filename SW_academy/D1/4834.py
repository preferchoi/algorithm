'''
3
5
49679
5
08271
10
7797946543
'''
TC = int(input())

for tc in range(1, 1 + TC):
    N = int(input())
    s = list(map(int, input()))

    keys = list(range(10))
    ans_dict = {key: 0 for key in keys}
    for i in s:
        ans_dict[i] += 1

    maxV, max_index = 0, 0

    for i in ans_dict:
        if maxV <= ans_dict[i]:
            maxV = ans_dict[i]
            max_index = i
    print(f'#{tc} {max_index} {maxV}')