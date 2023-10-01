def solution(want, number, discount):
    answer = 0
    want_number_dict = {k:0 for k in set(discount + want)}
    
    tmp = want_number_dict.copy()
    for w, n in zip(want, number):
        want_number_dict[w] += n
    
    for i in range(10):
        tmp[discount[i]] += 1
    
    for i in range(10, len(discount)):
        if want_number_dict == tmp:
            answer += 1
        tmp[discount[i-10]] -= 1
        tmp[discount[i]] += 1
    else:
        if want_number_dict == tmp:
            answer += 1
        
    return answer