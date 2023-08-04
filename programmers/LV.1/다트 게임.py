def solution(dartResult):
    answer = 0
    num = ''
    pre_num = 0
    input_num = True
    # print(ord('A'), ord('Z'), ord('#'), ord('*'))
    for c in dartResult:
        if ord('A') <= ord(c) <= ord('Z'):
            input_num = False
            num = int(num)
            if c == 'S':
                num **= 1
            elif c == 'D':
                num **= 2
            elif c == 'T':
                num **= 3
                
        elif ord(c) == ord('*'):
            num *= 2
            pre_num *= 2
            
        elif ord(c) == ord('#'):
            num *= -1
            
        else:
            if not input_num:
                answer += pre_num
                pre_num = num
                num = ''
                input_num = True
            num += c
        print(answer, pre_num, num)
    else:
        answer += pre_num + num
    return answer