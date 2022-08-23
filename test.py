def par(k, curSum):
    if k == N:
        # sumV = 0
        # for i in range(N):
        #     if result[i] == 1:
        #         sumV += lst[i]
        if curSum > 10:
            return
        if curSum == 10:
            for i in range(N):
                if result[i] == 1:
                    print(lst[i], end=' ')
            print()
    else:
        result[k] = 0
        par(k + 1, curSum)
        result[k] = 1
        par(k + 1, curSum[k])


def per(k):
    if k == N:
        print(result)
        for i in range(N):
            print(lst[result[i]], end=' ')
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            result[k] = i
            per(k + 1)
            visited[i] = False


lst = [range(1, 11)]
N = 10

0
result = [-1] * N
# par(0, 0)

visited = [False] * N

per(0)
