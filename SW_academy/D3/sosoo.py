# i = 10
# sosoo = [2, 3, 5, 7]
#
# while 100 >= i:
#     i += 1
#     count = 0
#
#     for K in sosoo:
#         if i % K == 0:
#             break
#         count += 1
#         if count == len(sosoo):
#             sosoo.append(i)
#
# for i in sosoo:
#     print(i, end=" ")

n = 1000000
sieve = [True] * n

m = int(n ** 0.5)
for i in range(2, m + 1):
    if sieve[i] == True:
        for j in range(i+i, n, i):
            sieve[j] = False
for x in [i for i in range(2, n) if sieve[i] == True]:
    print(x, end=" ")