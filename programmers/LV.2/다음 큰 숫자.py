def solution(n):

    tmp = bin(n).count('1')
    while True:
        n += 1
        if tmp == bin(n).count('1'):
            break

    return n