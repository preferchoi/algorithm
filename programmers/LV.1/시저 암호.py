def solution(s, n):
    answer = ''
    big_A, small_A = [chr(i) for i in range(ord('A'), ord('Z')+1)], [chr(i) for i in range(ord('a'), ord('z')+1)]
    for i in s:
        if i==' ':answer += ' '
        else:
            if i in small_A:answer += small_A[(small_A.index(i)+n)%26]
            else:answer += big_A[(big_A.index(i)+n)%26]
    return answer