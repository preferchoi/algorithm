'''
5
10
4 5
6 2
10 2
10
8 5
9 1
10 2
24
15 3
20 4
23 7
39
17 8
30 5
31 9
60
57 12
31 19
38 16

생각해봐야 할 때
게이트 입장시, 바로 앞 자리가 비어있고 입장인원이 짝수일 때 왼쪽오른쪽 봐야함

'''
from itertools import permutations






for tc in range(1, 1 + int(input())):
    N = int(input())
    idx_list = [False for _ in range(N + 1)]
    gate, person = [], []
    for _ in range(3):
        g, p = map(int, input().split())
        gate.append(g)
        person.append(p)




