def solution(my_string):
    answer = ''
    for i in my_string:
        if ord(i) < 97:
            answer += i.lower()
        else:
            answer += i.upper()
    return answer