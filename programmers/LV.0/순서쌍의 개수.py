def solution(n):
    answer = 1
    for i in range(1, n//2+1):
        if n / i == n // i:
            print(i)
            answer += 1
    return answer