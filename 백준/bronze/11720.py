N = int(input())
N_long = int(input())
sumV = 0
while N_long:
    sumV += N_long % 10
    N_long //= 10
print(sumV)