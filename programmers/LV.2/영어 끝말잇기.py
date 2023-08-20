def solution(n, words):
    answer = [words[0]]
    a, b = 1, 1
    for i in range(1, len(words)):
        b += 1
        if b > n:
            a += 1
            b = 1
        if words[i][0] != answer[-1][-1]:
            break
        if words[i] in answer:
            break
        answer.append(words[i])
    else:
        return 0, 0

    return b, a