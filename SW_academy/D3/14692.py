'''
5
2
3
10
50
100

'''
for tc in range(1, 1 + int(input())):
    N = int(input())
    print(f'#{tc}', end=' ')
    print('Bob' if N%2 else 'Alice')