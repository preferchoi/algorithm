def solution(answers):
    # 1번 1 - 2 - 3 - 4 - 5
    # 2번 2 - [1, 3, 4, 5]
    # 3번 3*2 - 1*2 - 2*2 - 4*2 - 5*2
    list_1, list_2, list_3 = [1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]
    answer_1,answer_2,answer_3 = 0,0,0
    
    for i in range(len(answers)):
        tmp = answers[i]
        if tmp == list_1[i%5]:answer_1 += 1
        if tmp == list_2[i%8]:answer_2 += 1
        if tmp == list_3[i%10]:answer_3 += 1
    
    answer = [answer_1,answer_2,answer_3]
    return [i+1 for i in range(3) if max(answer)==answer[i]]