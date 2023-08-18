def solution(x, n):
    answer = []
    return list(range(x,x*(n+1),x)) if x != 0 else [x for _ in range(n)]