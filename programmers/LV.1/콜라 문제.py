def solution(a, b, n):
    answer = 0
    while n//a:
        tmp1, tmp2 = n//a, n%a
        n = tmp1 * b + tmp2
        answer += tmp1 * b
    return answer