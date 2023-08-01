def solution(n):
    tmp = ''
    answer = 0
    pow = 1
    while n:
        tmp = str(n % 3) + tmp
        n //= 3
    
    pow = 1
    for i in tmp:
        answer += int(i) * pow
        pow *= 3

    
    return answer