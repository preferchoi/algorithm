def solution(sizes):
    bigger, smaller = [], []
    for w, h in sizes:
        if w > h:
            bigger.append(w)
            smaller.append(h)
        else:
            bigger.append(h)
            smaller.append(w)
            
    return max(bigger) * max(smaller)
