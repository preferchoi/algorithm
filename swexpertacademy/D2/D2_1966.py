T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    K = input().split(" ")

    # print(K)

    for i in range(N):
        K[i] = int(K[i])

    # print(K)

    for j in range(N-1):
        for i in range(N-1):
            if K[i] > K[i+1]:
                K[i], K[i+1] = K[i+1], K[i]

    print(f'#{test_case}', end=" ")
    for i in range(N):
        print(K[i], end=" ")
    print()