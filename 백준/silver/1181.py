N = int(input())

s_list = list(set([input() for _ in range(N)]))
s_list.sort()
for i in range(1, 51):

    for j in s_list:
        if len(j) == i:
            print(j)
