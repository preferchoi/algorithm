def solution(n):
    answer = 0
    if n % 6 == 0:
        answer = n//6
    elif n % 3 == 0:
        answer = n//3
    elif n % 2 == 0:
        answer = n//2
    else:
        answer = n
    return answer