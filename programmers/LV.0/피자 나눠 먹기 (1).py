def solution(n):
    answer = int(n / 7)
    if answer != n/7:
        answer += 1
    
    return answer