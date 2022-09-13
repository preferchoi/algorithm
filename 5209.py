'''
3
3
73 21 21
11 59 40
24 31 83
5
93 4 65 31 66
63 12 60 60 84
87 57 44 35 20
12 9 40 12 40
60 21 3 49 54
6
55 83 32 79 53 70
77 88 80 93 42 29
54 26 5 10 25 94
77 92 82 83 11 51
84 11 21 62 45 58
37 88 13 34 41 4

'''

from itertools import permutations

for tc in range(1, 1 + int(input())):
    N = int(input())
    N_list = [list(map(int, input().split())) for _ in range(N)]
    line_max = []
    cnt = 0
    for i in N_list:
        cnt += max(i)
        line_max.append(cnt)
    print(line_max)
    maxV = line_max[-1]
    for i in permutations(range(N), N):
        cnt = 0
        sumV = 0
        for j in i:
            sumV += N_list[cnt][j]
            cnt += 1

            if sumV >= line_max[cnt-1]:
                break

        if sumV < maxV:
            maxV = sumV

    print(f'#{tc} {maxV}')
