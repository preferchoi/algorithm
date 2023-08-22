def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    for a, b in zip(A, B[::-1]):
        answer += a * b
    return answer