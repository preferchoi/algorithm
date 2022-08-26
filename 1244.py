N = int(input())
N_list = list(map(int, input().split()))
M = int(input())

for q in range(M):
    per, num = map(int, input().split())
    num = num - 1
    if per == 1:
        for i in range(num, N, num + 1):
            if N_list[i] == 1:
                N_list[i] = 0
            else:
                N_list[i] = 1

    else:
        key = num if num < N - num else N - num
        tmp = []
        while key:
            if 0 <= num - key < N and 0 <= num + key < N:
                tmp = N_list[num-key:num+key]
                if N_list[num-key:num+key] == N_list[num-key:num+key][::-1]:
                    break
            key -= 1
        for i in range(num-key-1, num+key+2):
            if N_list[i]:
                N_list[i] = 0
            else:
                N_list[i] = 1

for i in range(0, len(N_list), 20):
    print(*N_list[i:i + 20])
