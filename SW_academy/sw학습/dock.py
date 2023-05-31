'''
3
5
20 23
17 20
23 24
4 14
8 18
10
14 23
2 19
1 22
12 24
21 23
6 15
20 24
1 4
6 15
15 16
15
18 19
2 7
11 15
13 16
23 24
2 14
13 22
20 23
13 19
7 15
5 21
20 24
16 22
17 21
9 24

'''

for test in range(int(input())):
    N = int(input())
    ship_list = []
    for i in range(N):
        ship_list.append(list(map(int, input().split(" "))))
    ship_list.sort()
    # print(ship_list)

    count = 0
    end_time = 0
    for i in ship_list:
        if count == 0:
            count += 1
            end_time = i[1]
        if end_time <= i[0]:
            # print(i)
            end_time = i[1]
            count += 1
        if end_time > i[0] and end_time > i[1]:
            end_time = i[1]
    print(f'#{test+1}', count)

'''

'''
