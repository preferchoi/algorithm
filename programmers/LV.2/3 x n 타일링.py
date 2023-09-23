def solution(n):
    tmp = [3, 11]
    # 점화식 = f(n) = f(n-2) * 4 - f(n-4)
    for i in range(n//2 - 2):
        tmp.append(tmp[-1]*4-tmp[-2])
    return tmp[n//2-1]% 1000000007