def solution(babbling):
    answer = 0
    
    for i in babbling:
        tmp = i
        while True:
            if tmp[:2] == 'ye' or tmp[:2] == 'ma':
                tmp = tmp[2:]
            elif tmp[:3] == 'aya' or tmp[:3] == 'woo':
                tmp = tmp[3:]
            else:
                break
            if tmp == '':
                answer += 1
                break
    return answer