def solution(n):
    answer = 0
    
    for i in range(4, n + 1):
        tmp = 1
        for j in range(1, i//2+1):
            if i % j == 0:
                tmp += 1
            if tmp >= 3:
                answer += 1
                break
    
    return answer