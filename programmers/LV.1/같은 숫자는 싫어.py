def solution(arr):
    answer = []
    pre = arr[0]
    for i in arr[1:]:
        if pre != i:
            answer.append(pre)
            pre = i
    else:
        answer.append(pre)

    return answer