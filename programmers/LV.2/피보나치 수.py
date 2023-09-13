def solution(n):
    tmp = [0, 1]
    for _ in range(n-1):
        tmp.append(tmp[-1] + tmp[-2])

    return tmp[-1] % 1234567