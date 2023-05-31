'''
5
0 1 1 3 2

'''
N = int(input())
N_list = list(map(int, input().split()))

ans = []
for i in range(N):
    ans.append(i + 1)
    l_ans = len(ans)
    for j in range(N_list[i]):
        ans[-j - 1], ans[-j - 2] = ans[-j - 2], ans[-j - 1]
print(*ans)
