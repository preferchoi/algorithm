'''
3
10
1 2 3 4 5 6 7 8 9 10
10
67 39 16 49 60 28 8 85 89 11
20
3 69 21 46 43 60 62 97 64 30 17 88 18 98 71 75 59 36 9 26

'''

for tc in range(1, 1 + int(input())):
    N = int(input())
    N_list = list(map(int, input().split()))

    ans = []
    for _ in range(5):
        ans.append(N_list.pop(N_list.index(max(N_list))))
        ans.append(N_list.pop(N_list.index(min(N_list))))
    print(f'#{tc}', end=' ')
    for i in ans:
        print(i, end=' ')
    print()