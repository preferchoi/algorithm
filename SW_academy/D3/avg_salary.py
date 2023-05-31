'''
3
7
15 15 15 15 15 15 15
10
1 1 1 1 1 1 1 1 1 100
7
2 7 1 8 2 8 4
'''


T = int(input())

for test in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    # print(a)

    # print(sum(a)/len(a))
    count = 0

    for i in range(len(a)):
        if sum(a)/len(a) >= a[i]:
            count += 1
    print(f'#{test}', count)