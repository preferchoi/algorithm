def solution(n):
    answer = 0
    s, e = 1,1
    tmp = 1
    

    while s <= n:
        if tmp < n:
            e += 1
            tmp += e
        elif tmp > n:
            tmp -= s
            s += 1
        else:
            tmp -= s
            s += 1
            answer += 1

    return answer