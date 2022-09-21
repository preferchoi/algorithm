N = int(input())

lst = [0] * 10001

for i in range(N):
    lst[int(input())] += 1

for i in range(len(lst)):
    for j in range(lst[i]):
        print(i)
