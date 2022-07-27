'''
2
3
A 10
B 7
C 5
4
B 20
C 19
E 18
R 17

'''

T = int(input())

for test in range(1, T+1):
    N = int(input())
    list = []
    for i in range(N):
        list.append(input().split(" "))
        list[i][1] = int(list[i][1])
    c_list = []
    for i in range(N):
        c_list.append([list[i][0]]*list[i][1])
    C_list = sum(c_list, [])
    count = 0
    print(f'#{test}')
    for i in range(len(C_list)):
        print(C_list[i], end="")
        count += 1
        if count == 10 and not i == len(C_list)-1:
            print()
            count = 0
    print()