'''
1
9550 9556 9550 9553 9558 9551 9551 9551
2
2419 2418 2423 2415 2422 2419 2420 2415
3
7834 7840 7840 7835 7841 7835 7835 7838
4
4088 4087 4090 4089 4093 4085 4090 4084
5
2945 2946 2950 2948 2942 2943 2948 2947
6
670 667 669 671 670 670 668 671
7
8869 8869 8873 8875 8870 8872 8871 8873
8
1709 1707 1712 1712 1714 1710 1706 1712
9
10239 10248 10242 10240 10242 10242 10245 10235
10
6580 6579 6574 6580 6583 6580 6577 6581

'''
for tc in range(1, 11):
    N = int(input())
    N_queue = list(map(int, input().split()))
    front, near = 0, 7
    cnt = 0
    while True:
        cnt += 1
        if cnt == 6:
            cnt = 1
        if N_queue[front] - cnt > 0:
            N_queue.append(N_queue[front] - cnt)
        else:
            N_queue.append(0)
            break
        front = front + 1
        near = near + 1
    print(f'#{tc}', end=' ')
    print(*N_queue[front+1:near+2])

