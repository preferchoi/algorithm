def solution(my_string):
    answer = ''
    tmp = []
    for i in my_string:
        tmp.append(i.lower())
    tmp.sort()
    for i in tmp:
        answer += i
    return answer