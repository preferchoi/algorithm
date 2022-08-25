N = int(input())
N_list = [int(input()) for _ in range(N)]
N_list.sort()
print(*N_list)
# 버블 정렬
# for _ in range(N):
#     for j in range(N-1):
#         if N_list[j] > N_list[j+1]:
#             N_list[j], N_list[j+1] = N_list[j+1], N_list[j]


#
# for i in range(N-1):
#     print(N_list[i:])
#     idx = N_list[i:].index(min(N_list[i:]))
#     N_list[i], N_list[i+idx-1] = N_list[i+idx-1], N_list[i]
#     print(i, idx, N_list)
# print(N_list)