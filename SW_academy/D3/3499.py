'''
3
6
A B C D E F
4
JACK QUEEN KING ACE
5
ALAKIR ALEXSTRASZA DR-BOOM LORD-JARAXXUS AVIANA

[광주_1반_최선호]
'''

for tc in range(1, 1 + int(input())):
    N = int(input())
    N_list = list(input().split())
    mid = (N + 1) // 2

    print(f'#{tc}',end=' ')
    for i in range(mid):
        print(N_list[i], end=' ')
        if i + mid < N:
            print(N_list[i + mid], end=' ')
    print()