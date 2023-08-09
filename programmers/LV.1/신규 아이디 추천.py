def solution(new_id):
    answer = new_id
    answer = answer.lower()
    
    tmp = []
    for idx in answer:
        if not(48 <= ord(idx) <= 57 or 97 <= ord(idx) <= 122 or ord(idx) == 45 or ord(idx) ==46 or ord(idx) == 95):
            tmp.append(idx)
    for i in tmp:
        answer = answer.replace(i, '')
    
    tmp = answer.replace('..', '.')
    while tmp != answer:
        answer = tmp
        tmp = answer.replace('..', '.')
    
    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:len(answer)-1]
    
    if not answer:
        answer = 'aaa'
    
    if len(answer) >= 16:
        answer = answer[:15]
    
    if answer[-1] == '.':
        answer = answer[:len(answer)-1]
    
    if len(answer) < 3:
        answer += answer[-1] * (3 - len(answer))
    
    print(answer)

    return answer