N_list = list(map(int, input().split()))

sumV = 0
for i in N_list:
    sumV += i ** 2
print(sumV % 10)
