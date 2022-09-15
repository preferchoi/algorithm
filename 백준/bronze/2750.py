'''
5
5
2
3
4
1

'''
n = int(input())
lst = [int(input()) for i in range(n)]

for i in range(n):
    for j in range(i, n):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

for i in lst:
    print(i)
