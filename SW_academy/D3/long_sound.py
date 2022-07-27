'''
2
wow
3
2 3 2
hoi
3
0 0 0
'''
for test_case in range(1, int(input())+1):
    word = list(input())

    ti = int(input())
    ma = list(map(int, input().split(" ")))
    ma.sort()
    ma.reverse()
    for i in range(ti):
        word.insert(ma[i], '-')
    print(f'#{test_case}', end=' ')
    for i in word:
        print(i, end="")
    print()
