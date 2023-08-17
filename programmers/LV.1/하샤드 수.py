def solution(x):
    answer = 0
    tmp = x 
    while tmp:
        answer += tmp % 10
        tmp //= 10
    answer = x / answer
    return True if answer == int(answer) else False