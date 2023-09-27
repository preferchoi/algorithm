def solution(n,a,b):
    answer = 1
    tmp = list(range(1, n+1))
    while True:
        tmp2 = []
        for i in range(0,len(tmp),2):
            t = tmp[i:i+2]
            if a in t and b in t:
                return answer
            elif a in t:
                tmp2.append(a)
            elif b in t:
                tmp2.append(b)
            else:
                tmp2.append(tmp[i])
        tmp = tmp2.copy()
        answer += 1

    return answer