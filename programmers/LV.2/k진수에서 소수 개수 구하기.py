import math

def solution(n, k):

    answer = 0

    tmp = ''
    while n != 0:
        tmp = str(n%k) + tmp
        n = n // k
    print(tmp)
    tmp = tmp.split('0')

    for i in tmp:
        if i != '' and i != '1':
            t = int(i)
            for j in range(2, int(t**0.5)+1):
                if t%j == 0:
                    break
            else:
                answer += 1

    return answer