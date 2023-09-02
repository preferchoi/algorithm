def solution(n):
    answer = 0
    
    tmp = [True for _ in range(n+1)]
    tmp[0], tmp[1] = False, False
    for i in range(2, int((n+1) ** 0.5) + 1):
        if tmp[i]:
            for j in range(i * i, (n+1), i):
                tmp[j] = False

    return sum(tmp)