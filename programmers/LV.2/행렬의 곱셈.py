def solution(arr1, arr2):
    answer = []
    verti, horiz = len(arr2[0]), len(arr1)
    
    for h in range(horiz):
        tmp = []
        for v in range(verti):
            tmp2 = 0
            for k in range(len(arr2)):
                tmp2 += arr1[h][k] * arr2[k][v]
            tmp.append(tmp2)
        answer.append(tmp)

    return answer
