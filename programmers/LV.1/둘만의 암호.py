def solution(s, skip, index):
    answer = ''
    # skip = 
    tmp = [chr(i) for i in range(ord('a'),ord('z')+1) if i not in [ord(i) for i in skip]]

    for i in s:
        answer += tmp[(tmp.index(i) + index)%len(tmp)]
    return answer