'''
3
3 6
5 15
5 10

'''
from itertools import combinations

for tc in range(1, 1 + int(input())):
    N, K = map(int, input().split())
    Q_list = [i for i in range(1, 13)]
    count = 0
    for i in list(combinations(Q_list, N)):
        if sum(i) == K:
            count += 1

    print(f'#{tc} {count}')