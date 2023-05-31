"""

1
3 5
1 5 3
3 6 -7 5 4

"""

T = int(input())
for test_case in range(1, T+1):
    N, M = 0, 0
    N, M = input().split(" ")
    N, M = int(N), int(M)
    # print("N:", N, "M:", M)

    N_list = input().split(" ")
    M_list = input().split(" ")

    for i in range(N):
        N_list[i] = int(N_list[i])
    for i in range(M):
        M_list[i] = int(M_list[i])


    # print("N_list:", N_list)
    # print("M_list:", M_list)

    if N < M:
        N_list, M_list = M_list, N_list
        N, M = M, N
#         print(f"N({N})이 M({M})보다 작음 ")
#         print("N_list:", N_list)
#         print("M_list:", M_list)
# #         큰 행렬이 위로 가게 만들었음
#     print("N:", N, "M:", M)

    # for i in N_list:
    #     for j in M_list:
    #         print(f"{i}*{j}={i*j}", end='\t')
    #     print()

    max = 0

    for i in range(N-M+1):
        sum = 0
        for j in range(M):
            sum += N_list[j+i]*M_list[j]
        if max < sum:
            max = sum
    print(f'#{test_case}', max)