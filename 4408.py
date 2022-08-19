'''
3
4
10 20
30 40
50 60
70 80
2
1 3
2 200
3
10 100
20 80
30 50

'''
for tc in range(1, 1 + int(input())):
    N = int(input())
    N_list = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        N_list[i] = [(N_list[i][0]+1)//2, (N_list[i][1])+1//2]
    N_list.sort()
    N_list = N_list[::-1]
    N_copy = N_list[:]

    cnt = 0
    while N_list:
        cnt += 1
        maxV = -1
        for i in range(len(N_list)-1, -1, -1):
            if N_list[i][0] > maxV:
                maxV = N_list[i][1]
                del N_copy[i]
        N_list = N_copy[:]

    print(f'#{tc} {cnt}')
