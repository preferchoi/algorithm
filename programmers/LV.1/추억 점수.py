def solution(name, yearning, photo):
    answer = []
    n_y_dict = {name[i]:yearning[i] for i in range(len(name))}
    print(n_y_dict)
    # print(name)
    # print(yearning)
    # print(photo)
    for i in photo:
        tmpV = 0
        for j in i:
            if j in name:
                tmpV += n_y_dict[j]
        answer.append(tmpV)
    return answer