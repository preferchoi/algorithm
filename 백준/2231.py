def finding(N):
    conut = 0

    for i in str(N):
        conut += 1

    for i in range(N - (9 * conut), N):
        if i < 0:
            i = 1

        sumV = i

        for j in str(i):
            sumV += int(j)

        if sumV == N:
            return i
    return 0


N = int(input())
print(finding(N))
