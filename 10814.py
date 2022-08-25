N = int(input())
N_list = [list(input().split()) for _ in range(N)]

# N_list.sort()
# N_list.reverse()

for i in range(N):  # 0, 1, 2
    for j in range(N-1, i, -1):  # 2, 1
        if int(N_list[j - 1][0]) > int(N_list[j][0]):
            N_list[j - 1], N_list[j] = N_list[j], N_list[j - 1]
    print(*N_list[i])

# for i in N_list:
#     print(*i)