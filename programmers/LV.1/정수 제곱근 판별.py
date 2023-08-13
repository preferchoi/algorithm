def solution(n):
    answer = n ** 0.5
    return -1 if answer != int(answer) else (answer + 1) **2