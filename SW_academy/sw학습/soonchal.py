'''
3
3
0 18 34
48 0 55
18 7 0
4
0 83 65 97
82 0 78 6
19 19 0 82
6 34 94 0
5
0 9 26 85 42
14 0 84 31 27
58 88 0 16 46
83 61 94 0 17
40 71 24 38 0

'''
'''
구역이 1, 2, 3, 4 있을 때
1에서 시작
끝에는 1로 돌아옴

1- @ - @ - @ - 1
2 3 4
2 4 3
3 2 4
3 4 2
4 2 3
4 3 2

list = [0]
list.append(N1) @@@ 1
list.append(N2) @@@ 2
list.append(N3) @@@ 3
list.append(0)
list = [0, 1, 2, 3, 0]
x축 = range(len(list)-1)
y축 = range(1, len(list))
sum = 0
for i, j in [range(len(list)-1), range(1, len(list))]:
    sum += list[i][j]
'''

'''
[1, 2, 3], []

[2,3][1]
[1,3][2]
[1,2][3]

[3][1,2]
[2][1,3]

[3][2,1]
[1][2,3]

[2][3,1]
[1][3,2]

[][1,2,3]
[][1,3,2]
[][2,1,3]
[][2,3,1]
[][3,1,2]
[][3,2,1]

'''
import itertools

for test in range(int(input())):
    N = int(input())
    N_list = []
    for i in range(N):
        N_list.append(list(map(int, input().split(" "))))
    # print(N_list)
    g_s = list(range(1, N))
    # 출발지 0 제외, 순찰지 리스트
    ans = list(itertools.permutations(g_s, N-1))
    mini = 9999999999
    for i in ans:
        a, c = 0, 0
        for j in i:
            a += N_list[c][j]
            c = j
        a += N_list[c][0]
        if mini > a:
            mini = a
    print(f'#{test+1}', mini)
