def solution(slice, n):
    answer = int(n / slice)
    if answer != n / slice:
        answer += 1
    return answer