n, m = 2, 2
# n, m = map(int, input().split())
mapp = ['_' for _ in range(5)]


for i in range(n):
    mapp[m + i] = n - i
    for j in mapp:
        print(j, end='')
    print()
    mapp[m + i] = '_'
else:
    print('_' * 5)
# for i in range(n, -1, -1):
#     mapp[m - 1 + (n - i)] = '_'
#     if not i:
#         for j in mapp:
#             print(j, end='')
#         print()
#         break
#     mapp[m + (n - i)] = i
#     for j in mapp:
#         print(j, end='')
#     print()
