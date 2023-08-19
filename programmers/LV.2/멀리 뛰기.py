def solution(n):
    answer = 0
    tmp = [1,2]
    for i in range(n-2):
        tmp.append(tmp[i] + tmp[i+1])
    return tmp[-1]%1234567 if n > 2 else tmp[n-1]

'''
n = 1 => 1
n = 2 => 2
n = 3 => 3
n = 4 => 5
n = 5 => 8
n = 6 => 13

피보나치 수열
'''