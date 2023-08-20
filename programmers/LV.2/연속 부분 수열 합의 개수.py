def solution(elements):
    answer = set()
    for i in range(len(elements)):
        for j in range(1, len(elements) + 1):
            if i + j < len(elements):
                answer.add(sum(elements[i:i+j]))
            else:
                answer.add(sum(elements[i:] + elements[:i + j - len(elements)]))
    return len(list(answer))